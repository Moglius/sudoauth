from django.db import models

from helpers.validators.model_validators import (validate_hostname,
    validate_path)


class SudoUser(models.Model):
    ''' https://www.sudo.ws/docs/man/1.8.17/sudoers.ldap.man/#sudoUser
    '''
    username = models.CharField(max_length=65, unique=True)
    built_in = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @classmethod
    def get_instance(cls, username):
        return cls.objects.get(username=username['username'])

    @classmethod
    def get_instances(cls, sudo_users) -> list:
        return_list = []
        for sudo_user in sudo_users:
            return_list.append(cls.objects.get(username=sudo_user['username']))
        return return_list

    def get_attached_sudorules(self):
        return list(self.sudorule_set.all())


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


class SudoRule(models.Model):
    name = models.CharField(max_length=50, unique=True)
    sudo_user = models.ManyToManyField(SudoUser)
    sudo_host = models.ManyToManyField(SudoHost)
    sudo_command = models.ManyToManyField(SudoCommand)
    run_as_user = models.ForeignKey(
        SudoUser,
        related_name='sudorule_runasuser_set',
        on_delete=models.CASCADE
    )
    run_as_group = models.ForeignKey(
        SudoUser,
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

    def get_ldap_name(self):
        return self.name.encode('utf-8')

    def get_ldap_run_as_user(self):
        return self.run_as_user.username.encode('utf-8')

    def get_ldap_run_as_group(self):
        return self.run_as_group.username.encode('utf-8')

    def get_ldap_sudouser_list(self):
        return [user.username.encode('utf-8') for user in self.sudo_user.all()]

    def get_ldap_command_list(self):
        return [command.full_command.encode('utf-8') for command in self.sudo_command.all()]

    def get_ldap_host_list(self):
        return [host.hostname.encode('utf-8') for host in self.sudo_host.all()]

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