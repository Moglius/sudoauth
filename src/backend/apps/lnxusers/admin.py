from django.contrib import admin

from .models import LnxGroup, LnxShell, LnxUser

# Register your models here.
admin.site.register(LnxGroup)
admin.site.register(LnxShell)
admin.site.register(LnxUser)
