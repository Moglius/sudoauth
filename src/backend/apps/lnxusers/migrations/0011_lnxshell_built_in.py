# Generated by Django 4.1.7 on 2023-03-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lnxusers', '0010_alter_lnxuser_login_shell_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnxshell',
            name='built_in',
            field=models.BooleanField(default=False),
        ),
    ]