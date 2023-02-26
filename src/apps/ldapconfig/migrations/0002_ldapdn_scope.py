# Generated by Django 4.1.7 on 2023-02-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldapconfig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ldapdn',
            name='scope',
            field=models.CharField(choices=[('OL', 'One Level'), ('SB', 'Subtree')], default='OL', max_length=2),
        ),
    ]