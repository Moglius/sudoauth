from django.db import models


class SudoUser(models.Model):
    ''' https://www.sudo.ws/docs/man/1.8.17/sudoers.ldap.man/#sudoUser
    '''
    username = models.CharField(max_length=65)


class SudoHost(models.Model):

    hostname = models.CharField(max_length=253) # maximum of 253 ASCII characters


class SudoCommand(models.Model):

    command = models.CharField(max_length=255)
    diggest = models.CharField(max_length=255, blank=True, null=True)


class SudoRule(models.Model):
    sudo_user = models.ForeignKey(SudoUser, on_delete=models.CASCADE)
    sudo_host = models.ForeignKey(SudoHost, on_delete=models.CASCADE)
    sudo_command = models.ManyToManyField(SudoCommand)
    run_as_user = models.ForeignKey(SudoUser, on_delete=models.CASCADE)
    run_as_group = models.ForeignKey(SudoUser, on_delete=models.CASCADE)
