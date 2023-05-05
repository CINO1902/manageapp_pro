# Generated by Django 4.0.6 on 2022-12-20 08:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("allocated_row", models.IntegerField()),
                ("service_index", models.IntegerField()),
                ("male_count", models.IntegerField(default=0)),
                ("female_count", models.IntegerField(default=0)),
                ("teenager_count", models.IntegerField(default=0)),
                ("children_count", models.IntegerField(default=0)),
                ("first_timer_count", models.IntegerField(default=0)),
                ("coverts_count", models.IntegerField(default=0)),
                ("vehicle_count", models.IntegerField(default=0)),
                ("motor_bikes_count", models.IntegerField(default=0)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Attendance",
                "verbose_name_plural": "Attendances",
                "ordering": ["-created_date"],
            },
        ),
    ]
