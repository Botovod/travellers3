# Generated by Django 2.2.5 on 2019-10-03 09:46

from django.db import migrations, models
import django.db.models.deletion
import vkapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('vkapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.PositiveIntegerField(default=0, null=True)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to=vkapp.models.set_image_folder)),
                ('album_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vkapp.Album')),
            ],
        ),
    ]