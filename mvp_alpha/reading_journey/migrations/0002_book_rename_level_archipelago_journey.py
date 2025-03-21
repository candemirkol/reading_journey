# Generated by Django 5.0.6 on 2024-07-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reading_journey", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("publication_date", models.DateField(blank=True, null=True)),
                ("genre", models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name="archipelago",
            old_name="level",
            new_name="journey",
        ),
    ]
