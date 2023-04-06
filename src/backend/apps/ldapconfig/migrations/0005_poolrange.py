# Generated by Django 4.1.7 on 2023-03-07 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldapconfig', '0004_ldapconfig_sudo_dn'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoolRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_min', models.PositiveBigIntegerField(default=50000, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(4294967295)])),
                ('pool_max', models.PositiveBigIntegerField(default=60000, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(4294967295)])),
            ],
        ),
    ]