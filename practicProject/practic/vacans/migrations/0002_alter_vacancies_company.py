# Generated by Django 5.0.6 on 2024-07-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vacans", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vacancies",
            name="company",
            field=models.CharField(max_length=45, verbose_name="Компания"),
        ),
    ]
