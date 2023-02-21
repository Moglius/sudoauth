from os import path
from django.db import models
from apps.sudoers.models import SudoUser
from helpers.validators.model_validators import (validate_path,
    validate_username)


class LnxShell(models.Model):
    shell = models.CharField(max_length=100, unique=True,
        validators=[validate_path])

    def __str__(self):
        return self.shell

    def save(self, *args, **kwargs):
        self.shell = path.normpath(self.shell).lower()
        super(LnxShell, self).save(*args, **kwargs)


class LnxGroup(models.Model):
    groupname = models.CharField(max_length=65,
        validators=[validate_username])
    gid_number = models.BigIntegerField(unique=True)

    related_group = models.ForeignKey(
        SudoUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.groupname

    def get_sudo_user_name(self):
        return f"%{self.groupname}"

    def set_sudo_user(self):
        self.related_group = SudoUser.objects.create(
            username=self.get_sudo_user_name())

    def set_sudo_user_name(self):
        self.related_group.username = self.get_sudo_user_name()
        self.related_group.save()


class LnxUser(models.Model):
    username = models.CharField(max_length=50, unique=True,
        validators=[validate_username]) # uid
    uid_number = models.BigIntegerField(unique=True)
    primary_group = models.ForeignKey(
        LnxGroup,
        on_delete=models.CASCADE
    )
    login_shell = models.ForeignKey(
        LnxShell,
        on_delete=models.CASCADE
    )
    home_dir = models.CharField(max_length=100,
        validators=[validate_path])
    gecos = models.CharField(max_length=64)

    related_user = models.ForeignKey(
        SudoUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

    def get_sudo_user_name(self):
        return self.username

    def set_sudo_user(self):
        self.related_user = SudoUser.objects.create(
            username=self.get_sudo_user_name())

    def set_sudo_user_name(self):
        self.related_user.username = self.get_sudo_user_name()
        self.related_user.save()

    def save(self, *args, **kwargs):
        self.home_dir = path.normpath(self.home_dir)
        super(LnxUser, self).save(*args, **kwargs)
