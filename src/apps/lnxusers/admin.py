from django.contrib import admin

from .models import LnxGroup, LnxShell, LnxUser


class LnxUserAdmin(admin.ModelAdmin):
    exclude = ('related_user',)


class LnxGroupAdmin(admin.ModelAdmin):
    exclude = ('related_group',)


# Register your models here.
admin.site.register(LnxGroup, LnxGroupAdmin)
admin.site.register(LnxShell)
admin.site.register(LnxUser, LnxUserAdmin)
