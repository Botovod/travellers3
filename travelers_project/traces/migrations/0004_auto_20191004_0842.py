# Generated by Django 2.2.5 on 2019-10-04 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0006_auto_20190927_1331'),
        ('traces', '0003_auto_20191004_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityInRoute',
            fields=[
                ('city_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geography.City')),
                ('position', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('geography.city',),
        ),
        migrations.RemoveField(
            model_name='routebycities',
            name='cities',
        ),
        migrations.AddField(
            model_name='routebycities',
            name='cities',
            field=models.ManyToManyField(blank=True, related_name='authored_books', to='traces.CityInRoute'),
        ),
    ]