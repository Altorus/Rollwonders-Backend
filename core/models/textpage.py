from django.db import models
from django.urls import reverse
from .base import BaseMenuItemModel, BaseSEOModel
from bs4 import BeautifulSoup


class TextPage(BaseMenuItemModel, BaseSEOModel):
    """Тектовая страница"""

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    is_generic_page = models.BooleanField(
        verbose_name="Является стандартной страницей",
        help_text="Снять галочку, если страница обрабатывается кастомной view",
        blank=True,
        default=False
    )

    def get_absolute_url(self):
        return reverse('text_page', kwargs={'page_slug': self.slug})
