# Generated by Django 4.0 on 2022-11-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_remove_motor_intensite_max_1ph_50_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor',
            name='condensateur',
            field=models.CharField(max_length=125, null=True, verbose_name='Condensateur'),
        ),
        migrations.AddField(
            model_name='motor',
            name='type_de_ref',
            field=models.CharField(max_length=125, null=True, verbose_name='Type de Réfrigiration'),
        ),
    ]