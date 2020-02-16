# Generated by Django 2.2.7 on 2020-02-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20200213_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Название социальной сети')),
                ('url', models.CharField(default='', max_length=255, verbose_name='Ссылка на социальную сеть')),
            ],
        ),
        migrations.RemoveField(
            model_name='mainpage',
            name='center_social_url',
        ),
        migrations.RemoveField(
            model_name='mainpage',
            name='left_social_url',
        ),
        migrations.RemoveField(
            model_name='mainpage',
            name='right_social_url',
        ),
    ]
