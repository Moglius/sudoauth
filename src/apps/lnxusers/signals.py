from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import LnxGroup, LnxUser


@receiver(pre_save, sender=LnxUser)
@receiver(pre_save, sender=LnxGroup)
def update_or_create_sudo_user(sender, instance, **kwargs):
    try:
        instance.set_sudo_user_name()
    except ObjectDoesNotExist:
        instance.set_sudo_user()
