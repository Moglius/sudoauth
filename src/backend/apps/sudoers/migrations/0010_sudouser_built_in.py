# Generated by Django 4.1.7 on 2023-03-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoers', '0009_sudorule_guidhex'),
    ]

    operations = [
        migrations.AddField(
            model_name='sudouser',
            name='built_in',
            field=models.BooleanField(default=False),
        ),
    ]