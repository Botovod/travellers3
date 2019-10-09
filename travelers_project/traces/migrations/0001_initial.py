# Generated by Django 2.2.5 on 2019-10-09 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitiesRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.City')),
            ],
        ),
        migrations.CreateModel(
            name='RouteBySights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Название маршрута')),
                ('description', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Маршрут по достопримечательностям',
                'verbose_name_plural': 'Маршруты по достопримечательностям',
            },
        ),
        migrations.CreateModel(
            name='SightsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traces.RouteBySights')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geography.Sight')),
            ],
        ),
        migrations.AddField(
            model_name='routebysights',
            name='sights',
            field=models.ManyToManyField(through='traces.SightsRelationship', to='geography.Sight', verbose_name='Достопримечательности маршрута'),
        ),
        migrations.CreateModel(
            name='RouteByCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Название маршрута')),
                ('description', models.TextField(default='')),
                ('cities', models.ManyToManyField(through='traces.CitiesRelationship', to='geography.City')),
            ],
            options={
                'verbose_name': 'Маршрут по городам',
                'verbose_name_plural': 'Маршруты по городам',
            },
        ),
        migrations.AddField(
            model_name='citiesrelationship',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traces.RouteByCities'),
        ),
    ]
