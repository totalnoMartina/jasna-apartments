# Generated by Django 3.2 on 2022-02-28 23:17

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartmentsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='more_images',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='another_image'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(choices=[('TONY', 'tony'), ('MATEA', 'matea'), ('MARTINA', 'martina')], max_length=10),
        ),
        migrations.DeleteModel(
            name='AppName',
        ),
    ]
