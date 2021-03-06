# Generated by Django 3.1.7 on 2021-06-29 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('brand', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km', models.IntegerField()),
                ('plaka', models.CharField(max_length=100, unique=True)),
                ('sase_no', models.CharField(max_length=100, unique=True)),
                ('renk', models.CharField(max_length=100)),
                ('vehicle_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.vehicle_model')),
            ],
        ),
    ]
