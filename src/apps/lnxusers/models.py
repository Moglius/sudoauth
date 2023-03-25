from os import path
from django.db import models
from django.apps import apps
from helpers.validators.model_validators import (validate_path,
    validate_username)


class LnxShell(models.Model):
    shell = models.CharField(max_length=100, unique=True,
        validators=[validate_path])
    built_in = models.BooleanField(default=False)

    def __str__(self):
        return self.shell

    def save(self, *args, **kwargs):
        self.shell = path.normpath(self.shell).lower()
        super(LnxShell, self).save(*args, **kwargs)

    def get_shell_name(self):
        return self.shell

    def is_built_in(self):
        return self.built_in

    def is_default_shell(self):
        return self.default_shell_set.all()

    def get_attached_lnxusers(self):
        return self.lnxuser_set.all()


class LnxGroup(models.Model):
    groupname = models.CharField(max_length=65,
        validators=[validate_username])
    gid_number = models.BigIntegerField(unique=True)
    guidhex = models.CharField(max_length=60)

    related_group = models.ForeignKey(
        'sudoers.SudoUser',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.groupname

    def get_sudo_user_name(self):
        return f"%{self.groupname}"

    def set_sudo_user(self):
        sudo_user = apps.get_model('sudoers.SudoUser')
        self.related_group = sudo_user.objects.create(
            username=self.get_sudo_user_name())

    def set_sudo_user_name(self):
        self.related_group.username = self.get_sudo_user_name()
        self.related_group.save()

    def get_gid_number(self):
        return str(self.gid_number)

    def get_guid(self):
        return self.guidhex

    def get_ldap_gid(self):
        return str(self.gid_number).encode('utf-8')

    def is_default_group(self):
        return self.default_group_set.all()

    def get_attached_lnxusers(self):
        return self.lnxuser_set.all()


class LnxUser(models.Model):
    username = models.CharField(max_length=50, unique=True,
        validators=[validate_username]) # uid
    uid_number = models.BigIntegerField(unique=True)
    primary_group = models.ForeignKey(
        LnxGroup,
        on_delete=models.DO_NOTHING
    )
    login_shell = models.ForeignKey(
        LnxShell,
        on_delete=models.DO_NOTHING
    )
    home_dir = models.CharField(max_length=100,
        validators=[validate_path])
    gecos = models.CharField(max_length=64)

    related_user = models.ForeignKey(
        'sudoers.SudoUser',
        on_delete=models.CASCADE
    )
    guidhex = models.CharField(max_length=60)

    def __str__(self):
        return self.username

    def get_sudo_user_name(self):
        return self.username

    def get_guid(self):
        return self.guidhex

    def set_sudo_user(self):
        sudo_user = apps.get_model('sudoers.SudoUser')
        self.related_user = sudo_user.objects.create(
            username=self.get_sudo_user_name())

    def set_sudo_user_name(self):
        self.related_user.username = self.get_sudo_user_name()
        self.related_user.save()

    def set_shell(self, shell):
        self.login_shell = shell
        self.save()

    def set_group(self, group):
        self.primary_group = group
        self.save()

    def save(self, *args, **kwargs):
        self.home_dir = path.normpath(self.home_dir)
        super(LnxUser, self).save(*args, **kwargs)

    def get_ldap_gid(self):
        return str(self.primary_group.gid_number).encode('utf-8')

    def get_ldap_uid(self):
        return str(self.uid_number).encode('utf-8')

    def get_ldap_gecos(self):
        return self.gecos.encode('utf-8')

    def get_ldap_homedir(self):
        return self.home_dir.encode('utf-8')

    def get_ldap_shell(self):
        return self.login_shell.shell.encode('utf-8')
