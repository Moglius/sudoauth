from os import path
from django.db import models

from apps.sudoers.models import SudoUser
from helpers.validators.model_validators import validate_path


class LnxShell(models.Model):
    shell = models.CharField(max_length=100, unique=True,
        validators=[validate_path])

    def __str__(self):
        return self.shell

    def save(self, *args, **kwargs):
        self.shell = path.normpath(self.shell).lower()
        super(LnxShell, self).save(*args, **kwargs)


class LnxGroup(models.Model):
    groupname = models.CharField(max_length=65)
    gid_number = models.BigIntegerField(unique=True)

    related_group = models.ForeignKey(
        SudoUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.groupname

    def save(self, *args, **kwargs):
        self.related_group = SudoUser.objects.get_or_create(
            username=f"%{self.groupname}")[0] # Tuple (obj, created)
        super(LnxGroup, self).save(*args, **kwargs)


class LnxUser(models.Model):
    username = models.CharField(max_length=50) # uid
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

    def save(self, *args, **kwargs):
        self.related_user = SudoUser.objects.get_or_create(
            username=self.username)[0] # Tuple (obj, created)
        self.home_dir = path.normpath(self.home_dir)
        super(LnxUser, self).save(*args, **kwargs)
