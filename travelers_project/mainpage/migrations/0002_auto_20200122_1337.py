# Generated by Django 2.2.7 on 2020-01-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Название страницы'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='video_picture',
            field=models.ImageField(default='image/v1.jpg', upload_to='video_pics/', verbose_name='Превью видео'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='main_banner',
            field=models.ImageField(upload_to='banners/', verbose_name='Баннер'),
        ),
    ]