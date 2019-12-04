# Generated by Django 2.2.7 on 2019-12-04 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0006_sightphoto_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='geography.Region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Адрес'),
        ),
    ]
