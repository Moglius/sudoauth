# Generated by Django 4.1.7 on 2023-02-21 20:17

from django.db import migrations, models
import helpers.validators.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('lnxusers', '0006_alter_lnxuser_home_dir_alter_lnxuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lnxgroup',
            name='groupname',
            field=models.CharField(max_length=65, validators=[helpers.validators.model_validators.validate_username]),
        ),
        migrations.AlterField(
            model_name='lnxuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[helpers.validators.model_validators.validate_username]),
        ),
    ]
