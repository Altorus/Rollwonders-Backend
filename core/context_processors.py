import logging

from django.utils.functional import SimpleLazyObject

from . import models

logger = logging.getLogger(__name__)


def site_settings(request):

    def get_settings_or_empty():
        try:
            return models.SiteSettings.get()
        except (models.SiteSettings.DoesNotExist, models.SiteSettings.MultipleObjectsReturned) as e:
            logger.warning("Got error when loading SiteSettings, use an empty settings instead")
            return models.SiteSettings()

    return {
        "site_settings": SimpleLazyObject(get_settings_or_empty),
    }


def company_contacts(request):
    return {
        "contacts": models.CompanyContacts.objects.first()
    }