# Generated by Django 4.2.1 on 2023-10-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_tracability", "0007_alter_action_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
