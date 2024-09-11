from django.db import models


class SiteSettings(models.Model):
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

    robots = models.TextField("robots.txt", blank=True)
    favicon = models.ImageField("Favicon", upload_to="favicon", blank=True)
    extra_head_html = models.TextField(blank=True)
    extra_body_html = models.TextField(blank=True)
    about_video = models.FileField(upload_to="videos/", blank=True, verbose_name="Видеобзор бота")

    @classmethod
    def get(cls):
        if not hasattr(cls, "_cached_obj"):
            cls._cached_obj = cls.objects.get()
        return cls._cached_obj

    def __str__(self):
        return "Настройки сайта"


class CompanyContacts(models.Model):
    phone = models.CharField(verbose_name="Телефон", max_length=16, blank=True)
    tg_contact = models.CharField(verbose_name="Ссылка на телеграм", help_text="Например @rollwonders)", blank=True,
                                  null=True, max_length=256)

    class Meta:
        verbose_name = "Контакты компании"
        verbose_name_plural = "Контакты компании"

    def __str__(self):
        return "Контакты компании"
