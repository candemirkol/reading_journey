# Generated by Django 5.0.6 on 2024-08-17 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reading_journey", "0004_archipelago_description_island_description"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
    ]
