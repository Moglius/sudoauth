from django.contrib import admin

from .models import (
    SudoUser,
    SudoHost,
    SudoCommand,
    SudoRule
)

# Register your models here.
admin.site.register(SudoUser)
admin.site.register(SudoHost)
admin.site.register(SudoCommand)
admin.site.register(SudoRule)
