# Generated by Django 4.1.7 on 2023-04-23 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ldapconfig", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ldapconfig",
            name="nis_netgroup_dn",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nis_netgroup_config_set",
                to="ldapconfig.ldapdn",
            ),
            preserve_default=False,
        ),
    ]
