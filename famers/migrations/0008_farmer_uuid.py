# Generated by Django 4.0.5 on 2023-02-23 09:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('famers', '0007_alter_farmer_options_alter_farmer_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
