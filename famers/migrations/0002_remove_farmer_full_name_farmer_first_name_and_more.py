# Generated by Django 4.1.7 on 2023-02-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("famers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="farmer",
            name="full_name",
        ),
        migrations.AddField(
            model_name="farmer",
            name="first_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="farmer",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="farmer_set", to="auth.group"
            ),
        ),
        migrations.AddField(
            model_name="farmer",
            name="is_superuser",
            field=models.BooleanField(
                default=False,
                help_text="Designates that this user has all permissions without explicitly assigning them.",
                verbose_name="superuser status",
            ),
        ),
        migrations.AddField(
            model_name="farmer",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="farmer",
            name="last_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="farmer",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True, related_name="farmer_set", to="auth.permission"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="phone_no",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="farmer",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="farmer",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="farmer",
            name="phone",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
