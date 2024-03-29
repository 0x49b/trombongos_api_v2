# Generated by Django 4.2.7 on 2023-11-09 14:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20220419_1020"),
    ]

    operations = [
        migrations.CreateModel(
            name="TourCalendar",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Tour Kalender",
                "verbose_name_plural": "Tour Kalender",
            },
        ),
    ]
