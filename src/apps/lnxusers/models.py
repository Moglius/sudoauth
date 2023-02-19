from django.db import models

from apps.sudoers.models import SudoUser


class LnxShell(models.Model):
    shell = models.CharField(max_length=100)


class LnxGroup(models.Model):
    groupname = models.CharField(max_length=65)
    gid_number = models.BigIntegerField()

    related_group = models.ForeignKey(
        SudoUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.groupname


class LnxUser(models.Model):
    username = models.CharField(max_length=50) # uid
    uid_number = models.BigIntegerField()
    gid_number = models.ForeignKey(
        LnxGroup,
        on_delete=models.CASCADE
    )
    login_shell = models.ForeignKey(
        LnxShell,
        on_delete=models.CASCADE
    )
    home_dir = models.CharField(max_length=100)
    gecos = models.CharField(max_length=64)

    related_user = models.ForeignKey(
        SudoUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username
