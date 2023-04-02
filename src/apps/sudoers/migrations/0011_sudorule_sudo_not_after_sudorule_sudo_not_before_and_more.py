# Generated by Django 4.1.7 on 2023-03-26 14:09

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sudoers', '0010_sudouser_built_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudorule',
            name='sudo_not_after',
            field=models.DateField(default=datetime.datetime(9999, 4, 10, 0, 0)),
        ),
        migrations.AddField(
            model_name='sudorule',
            name='sudo_not_before',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sudorule',
            name='sudo_order',
            field=models.IntegerField(default=0),
        ),
    ]