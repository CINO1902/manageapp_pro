# Generated by Django 4.0.6 on 2023-01-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="allocated_row",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="children_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="coverts_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="female_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="first_timer_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="male_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="motor_bikes_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="service_index",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="teenager_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="vehicle_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
