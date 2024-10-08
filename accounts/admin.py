from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class SiteSettingsAdmin(admin.ModelAdmin):
    readonly_fields = ('telegram_id',)
