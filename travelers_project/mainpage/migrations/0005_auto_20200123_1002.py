# Generated by Django 2.2.7 on 2020-01-23 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20200122_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpage',
            options={'ordering': ['title'], 'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главные страницы'},
        ),
    ]
