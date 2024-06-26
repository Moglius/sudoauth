from django.contrib import admin

from .models import DNSHost, LDAPConfig, LDAPDn, PoolRange


class LDAPConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not LDAPConfig.objects.exists()


admin.site.register(LDAPConfig, LDAPConfigAdmin)
admin.site.register(DNSHost)
admin.site.register(PoolRange)
admin.site.register(LDAPDn)
