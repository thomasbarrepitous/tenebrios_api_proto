# Generated by Django 4.2.1 on 2023-10-14 07:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api_tracability", "0005_alter_action_recolte_nb"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="NourrisageHumide",
            new_name="NourrissageHumide",
        ),
        migrations.RenameModel(
            old_name="NourrisageSon",
            new_name="NourrissageSon",
        ),
    ]
