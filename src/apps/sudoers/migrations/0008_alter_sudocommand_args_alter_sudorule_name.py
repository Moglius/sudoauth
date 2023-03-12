# Generated by Django 4.1.7 on 2023-03-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoers', '0007_alter_sudouser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudocommand',
            name='args',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sudorule',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
