# Generated by Django 4.0.5 on 2023-02-22 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('famers', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarkitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='famers.product'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
