from django.db import models

from helpers.validators.model_validators import (validate_hostname,
    validate_path)


class SudoHost(models.Model):

    hostname = models.CharField(max_length=253, unique=True,
        validators=[validate_hostname]) # maximum of 253 ASCII characters

    def __str__(self):
        return self.hostname

    @classmethod
    def get_instances(cls, sudo_hosts) -> list:
        return_list = []
        for sudo_host in sudo_hosts:
            return_list.append(cls.objects.get(hostname=sudo_host['hostname']))
        return return_list

    def get_ldap_value(self):
        return self.hostname.encode()


class SudoHostGroup(models.Model):

    name = models.CharField(max_length=50, unique=True)
    servers = models.ManyToManyField(SudoHost)
    nested = models.ManyToManyField('self', symmetrical=False,
        related_name='parents', blank=True)
    guidhex = models.CharField(max_length=60, editable=False)

    def __str__(self):
        return self.name

    def get_ldap_value(self):
        return f"+{self.name}".encode()

    def get_ldap_name(self):
        return self.name.encode()

    def get_ldap_nis_triple(self):
        return [f"({server.hostname},,)".encode() for server in self.servers.all()]

    def get_ldap_nis_member(self):
        return [hostgroup.get_ldap_name() for hostgroup in self.nested.all()]


class SudoCommand(models.Model):

    command = models.CharField(max_length=255,
        validators=[validate_path])
    args = models.CharField(max_length=255, blank=True)
    diggest = models.CharField(max_length=255, blank=True, null=True)

    @property
    def full_command(self):
        full_command = ''
        if self.diggest: full_command += f"{self.diggest} "
        full_command += f"{self.command}"
        if self.args: full_command += f" {self.args}"
        return full_command

    def __str__(self):
        return self.full_command

    @classmethod
    def get_instances(cls, sudo_commands) -> list:
        return_list = []
        for sudo_command in sudo_commands:
            return_list.append(cls.objects.get(command=sudo_command['command']))
        return return_list

    def get_ldap_value(self):
        return self.full_command.encode()


class SudoCommandRole(models.Model):

    name = models.CharField(max_length=50, unique=True)
    commands = models.ManyToManyField(SudoCommand)

    def __str__(self):
        return self.name

    def get_ldap_value(self):
        return [command.get_ldap_value() for command in self.commands.all()]


class SudoRule(models.Model):
    name = models.CharField(max_length=50, unique=True)

    sudo_user_users = models.ManyToManyField('lnxusers.LnxUser')
    sudo_user_groups = models.ManyToManyField('lnxusers.LnxGroup')

    sudo_host_servers = models.ManyToManyField(SudoHost)
    sudo_host_groups = models.ManyToManyField(SudoHostGroup)

    sudo_command = models.ManyToManyField(SudoCommand)
    sudo_command_role = models.ManyToManyField(SudoCommandRole)

    run_as_user = models.ForeignKey(
        'lnxusers.LnxUser',
        related_name='sudorule_runasuser_set',
        on_delete=models.CASCADE
    )
    run_as_group = models.ForeignKey(
        'lnxusers.LnxGroup',
        related_name='sudorule_runasgroup_set',
        on_delete=models.CASCADE
    )
    guidhex = models.CharField(max_length=60, editable=False)
    sudo_order = models.IntegerField(blank=True, null=True,
        help_text="Note: priority order, bigger values more priority.")
    sudo_not_before = models.DateField(blank=True, null=True,
        help_text="Note: This is the start date.")
    sudo_not_after = models.DateField(blank=True, null=True,
        help_text="Note: This is the expiration date.")

    def __str__(self):
        return self.name

    def set_default_runas_group(self, lnxgroup, default_group):
        if self.run_as_group == lnxgroup:
            self.run_as_group = default_group
            self.save()

    def set_default_runas_user(self, lnxuser, default_user):
        if self.run_as_user == lnxuser:
            self.run_as_user = default_user
            self.save()

    def get_ldap_name(self):
        return self.name.encode('utf-8')

    def get_ldap_run_as_user(self):
        return self.run_as_user.get_ldap_username()

    def get_ldap_run_as_group(self):
        return self.run_as_group.get_ldap_run_as_group()

    def get_ldap_sudouser_list(self):
        sudo_users = [user.get_ldap_username() for user in self.sudo_user_users.all()]
        for group in self.sudo_user_groups.all():
            sudo_users.append(group.get_ldap_groupname())
        return sudo_users

    def get_ldap_command_list(self):
        commands = set()
        commands.update([command.get_ldap_value() for command in self.sudo_command.all()])
        for command_role in self.sudo_command_role.all():
            commands.update(command_role.get_ldap_value())
        return list(commands)

    def get_ldap_host_list(self):
        hosts = [host.get_ldap_value() for host in self.sudo_host_servers.all()]
        for host_group in self.sudo_host_groups.all():
            hosts.append(host_group.get_ldap_value())
        return hosts

    def get_ldap_not_after(self):
        if self.sudo_not_after:
            return f"{self.sudo_not_after.strftime('%Y%m%d')}000000.0Z".encode('utf-8')
        return None

    def get_ldap_not_before(self):
        if self.sudo_not_before:
            return f"{self.sudo_not_before.strftime('%Y%m%d')}000000.0Z".encode('utf-8')
        return None

    def get_ldap_order(self):
        if self.sudo_order:
            return str(self.sudo_order).encode('utf-8')
        return None
