# Generated by Django 2.2.5 on 2019-09-06 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['title'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['title'], 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterModelOptions(
            name='sectionofsights',
            options={'ordering': ['title'], 'verbose_name': 'Раздел достопримечательностей', 'verbose_name_plural': 'Разделы достопримечательностей'},
        ),
        migrations.AlterModelOptions(
            name='sight',
            options={'ordering': ['title'], 'verbose_name': 'Достопримечательность', 'verbose_name_plural': 'Достопримечтельности'},
        ),
        migrations.AlterModelOptions(
            name='typeofsights',
            options={'ordering': ['title'], 'verbose_name': 'Тип достопримечательности', 'verbose_name_plural': 'Типы достопримечательностей'},
        ),
    ]