# Generated by Django 2.2.7 on 2020-02-10 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20200124_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighttrip',
            old_name='route_by_sights',
            new_name='route',
        ),
    ]