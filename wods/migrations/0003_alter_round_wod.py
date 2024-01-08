# Generated by Django 4.2.7 on 2023-12-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wods", "0002_remove_wod_rounds_round_repetitions_round_wod_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="round",
            name="wod",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rounds",
                to="wods.wod",
            ),
        ),
    ]