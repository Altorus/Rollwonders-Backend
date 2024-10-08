# Generated by Django 5.1.1 on 2024-09-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_ingredientcategory_ingredient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name': 'Настройки', 'verbose_name_plural': 'Настройки'},
        ),
        migrations.RemoveField(
            model_name='companycontacts',
            name='address',
        ),
        migrations.RemoveField(
            model_name='companycontacts',
            name='address_html_code',
        ),
        migrations.RemoveField(
            model_name='companycontacts',
            name='email',
        ),
        migrations.RemoveField(
            model_name='companycontacts',
            name='requisites',
        ),
        migrations.AddField(
            model_name='companycontacts',
            name='tg_contact',
            field=models.CharField(blank=True, help_text='Например @rollwonders)', max_length=256, null=True, verbose_name='Ссылка на телеграм'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='about_video',
            field=models.FileField(blank=True, upload_to='videos/', verbose_name='Видеобзор бота'),
        ),
    ]
