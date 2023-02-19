from django.contrib import admin

from .models import (
    LnxGroup,
    LnxShell,
    LnxUser
)


class LnxUserAdmin(admin.ModelAdmin):
    exclude = ('related_user',)


# Register your models here.
admin.site.register(LnxGroup)
admin.site.register(LnxShell)
admin.site.register(LnxUser, LnxUserAdmin)
