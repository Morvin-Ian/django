# Generated by Django 4.0.5 on 2023-02-23 09:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('famers', '0004_alter_farmer_options_alter_farmer_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]