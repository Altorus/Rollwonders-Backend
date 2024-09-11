import re

from django.contrib.auth import models as auth_models
from django.db import models


class User(auth_models.AbstractUser):
    telegram_id = models.IntegerField(unique=True, blank=True, null=True, verbose_name="id пользователя в Tg")
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True, null=True)

    @staticmethod
    def get_clean_phone(phone: str) -> str:
        return re.sub(r'[+|\(|\)|\-|\s]', '', phone)
