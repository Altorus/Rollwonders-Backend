# Generated by Django 4.2.3 on 2023-07-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_companycontacts_rename_contactsrecord_extrafields_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=64, verbose_name='Фамилия')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Заявка на обратную связь',
                'verbose_name_plural': 'Заявки на обратную связь',
            },
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='bitrix_lead_title_template',
            field=models.CharField(default='', help_text='Можно использовать просто строку, или шаблон django</br>Пример: "Заявка на обратную связь от {{ phone }}"</br>Можно использовать {% if ... %} {% endif %}</br>Доступные переменные: first_name, last_name, phone, email', max_length=64, verbose_name='Шаблон заголовка лида в битрикс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='bitrix_webhook_url',
            field=models.URLField(blank=True, default='', help_text='Оставьте пустым, чтобы отключить интеграцию с битрикс'),
        ),
        migrations.AlterField(
            model_name='companycontacts',
            name='address',
            field=models.CharField(blank=True, max_length=128, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='companycontacts',
            name='address_html_code',
            field=models.TextField(blank=True, verbose_name='HTML код для вставки карты'),
        ),
        migrations.AlterField(
            model_name='companycontacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='companycontacts',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='companycontacts',
            name='requisites',
            field=models.TextField(blank=True, verbose_name='Реквизиты'),
        ),
    ]
