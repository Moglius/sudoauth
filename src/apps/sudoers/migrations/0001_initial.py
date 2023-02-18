# Generated by Django 4.1.7 on 2023-02-18 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SudoCommand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=255)),
                ('diggest', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SudoHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=253)),
            ],
        ),
        migrations.CreateModel(
            name='SudoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='SudoRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_as_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sudorule_runasgroup_set', to='sudoers.sudouser')),
                ('run_as_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sudorule_runasuser_set', to='sudoers.sudouser')),
                ('sudo_command', models.ManyToManyField(to='sudoers.sudocommand')),
                ('sudo_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sudoers.sudohost')),
                ('sudo_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sudoers.sudouser')),
            ],
        ),
    ]
