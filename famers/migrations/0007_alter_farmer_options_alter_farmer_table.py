# Generated by Django 4.0.5 on 2023-02-23 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('famers', '0006_remove_farmer_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farmer',
            options={'verbose_name': 'Farmer', 'verbose_name_plural': 'Farmers'},
        ),
        migrations.AlterModelTable(
            name='farmer',
            table='Farmer',
        ),
    ]