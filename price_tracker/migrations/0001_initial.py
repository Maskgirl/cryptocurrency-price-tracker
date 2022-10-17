# Generated by Django 4.1.2 on 2022-10-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CoinPrice",
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
                ("timestamp", models.DateTimeField()),
                ("price", models.FloatField()),
                ("coin", models.CharField(max_length=13)),
                ("currency", models.CharField(max_length=5)),
            ],
        ),
    ]
