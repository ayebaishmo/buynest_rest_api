# Generated by Django 4.2.2 on 2025-05-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fulfilment",
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
                ("order_id", models.IntegerField()),
                ("fulfilled", models.BooleanField(default=False)),
                ("fulfilled_on", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
