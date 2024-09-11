from django.contrib import admin

from core import models, constants
from . import mixins


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(mixins.SingleObjectAdminMixin, admin.ModelAdmin):
    pass


@admin.register(models.CompanyContacts)
class CompanyContactsAdmin(mixins.SingleObjectAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(models.TextPage, admin.ModelAdmin)
admin.site.register(models.TelegramBotCredentials, admin.ModelAdmin)
