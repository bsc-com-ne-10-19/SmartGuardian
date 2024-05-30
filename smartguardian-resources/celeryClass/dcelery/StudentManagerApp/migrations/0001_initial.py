# Generated by Django 5.0.4 on 2024-05-04 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DeviceApp', '0002_locationdata_phonenumbers_delete_locationmanager_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('primary_location', models.CharField(default='', max_length=255)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=10)),
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DeviceApp.phonenumbers')),
            ],
        ),
    ]
