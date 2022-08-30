# Generated by Django 4.0 on 2022-08-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_remove_motor_cylindre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motor',
            name='intensite_max_1PH_50',
        ),
        migrations.RemoveField(
            model_name='motor',
            name='intensite_max_3PH_50',
        ),
        migrations.RemoveField(
            model_name='motor',
            name='photo',
        ),
        migrations.AddField(
            model_name='motor',
            name='dm_aspi',
            field=models.CharField(max_length=125, null=True, verbose_name="Diamètre d'aspiration en pouce"),
        ),
        migrations.AddField(
            model_name='motor',
            name='dm_refou',
            field=models.CharField(max_length=125, null=True, verbose_name='Diamètre de refoulement en pouce'),
        ),
        migrations.AddField(
            model_name='motor',
            name='i_max',
            field=models.CharField(max_length=125, null=True, verbose_name='Intensité max'),
        ),
        migrations.AddField(
            model_name='motor',
            name='q_huile',
            field=models.CharField(max_length=125, null=True, verbose_name="Quantité d'huile"),
        ),
        migrations.AddField(
            model_name='motor',
            name='refri',
            field=models.CharField(max_length=125, null=True, verbose_name='Réfrigération'),
        ),
    ]
