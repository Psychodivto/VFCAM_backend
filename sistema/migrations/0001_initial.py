# Generated by Django 5.0 on 2023-12-20 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Userprofile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foto_perfil",
                    models.ImageField(blank=True, null=True, upload_to="foto_perfil"),
                ),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("direccion", models.CharField(blank=True, max_length=100, null=True)),
                ("google_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
                ("anios", models.IntegerField(default=0)),
                ("peso", models.IntegerField(default=0)),
                ("imc", models.IntegerField(default=0)),
                ("objetivo", models.CharField(max_length=200)),
                ("cuentame", models.CharField(max_length=500)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sistema.userprofile",
                    ),
                ),
            ],
        ),
    ]