# Generated by Django 4.2.6 on 2024-04-05 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_sitesettings_bitrix_lead_title_template_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpage',
            name='is_generic_page',
            field=models.BooleanField(blank=True, default=False, help_text='Снять галочку, если страница обрабатывается кастомной view', verbose_name='Является стандартной страницей'),
        ),
        migrations.AlterField(
            model_name='textpage',
            name='menu_position',
            field=models.IntegerField(blank=True, default=0, verbose_name='Позиция в меню'),
        ),
    ]
