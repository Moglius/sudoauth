from django.contrib import admin

from .models import SudoCommand, SudoCommandRole, SudoHost, SudoHostGroup, SudoRule

# Register your models here.
admin.site.register(SudoHost)
admin.site.register(SudoCommand)
admin.site.register(SudoRule)
admin.site.register(SudoCommandRole)
admin.site.register(SudoHostGroup)
