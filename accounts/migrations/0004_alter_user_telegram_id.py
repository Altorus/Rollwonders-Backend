# Generated by Django 5.1.1 on 2024-09-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=24, null=True, unique=True, verbose_name='id пользователя в Tg'),
        ),
    ]
