# Generated by Django 4.1.7 on 2023-02-20 20:19

from django.db import migrations, models
import helpers.validators.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('sudoers', '0005_alter_sudohost_hostname'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudocommand',
            name='args',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sudocommand',
            name='command',
            field=models.CharField(max_length=255, validators=[helpers.validators.model_validators.validate_path]),
        ),
    ]
