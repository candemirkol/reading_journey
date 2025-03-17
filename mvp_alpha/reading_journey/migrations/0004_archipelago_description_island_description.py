# Generated by Django 5.0.6 on 2024-08-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reading_journey", "0003_lessoncompletion"),
    ]

    operations = [
        migrations.AddField(
            model_name="archipelago",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="island",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
