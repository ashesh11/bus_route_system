# Generated by Django 4.1.6 on 2023-02-13 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=100)),
                ('bus_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=100)),
                ('route_number', models.CharField(max_length=100)),
                ('buses', models.ManyToManyField(through='detail.BusRoute', to='detail.bus')),
            ],
        ),
        migrations.AddField(
            model_name='busroute',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='routes',
            field=models.ManyToManyField(through='detail.BusRoute', to='detail.route'),
        ),
        migrations.AlterUniqueTogether(
            name='busroute',
            unique_together={('bus', 'from_time', 'to_time')},
        ),
    ]