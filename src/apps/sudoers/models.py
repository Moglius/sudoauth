from django.db import models

from helpers.validators.model_validators import (validate_hostname,
    validate_path)


class SudoUser(models.Model):
    ''' https://www.sudo.ws/docs/man/1.8.17/sudoers.ldap.man/#sudoUser
    '''
    username = models.CharField(max_length=65)

    def __str__(self):
        return self.username


class SudoHost(models.Model):

    hostname = models.CharField(max_length=253, unique=True,
        validators=[validate_hostname]) # maximum of 253 ASCII characters

    def __str__(self):
        return self.hostname


class SudoCommand(models.Model):

    command = models.CharField(max_length=255,
        validators=[validate_path])
    args = models.CharField(max_length=255)
    diggest = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.diggest} {self.command}" if self.diggest else self.command


class SudoRule(models.Model):
    name = models.CharField(max_length=50)
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

    def __str__(self):
        return self.name
