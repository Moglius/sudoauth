# Generated by Django 4.1.7 on 2023-02-25 13:39

from django.db import migrations, models
import helpers.validators.model_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DNSHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=253, unique=True, validators=[helpers.validators.model_validators.validate_host_ip])),
            ],
        ),
        migrations.CreateModel(
            name='LDAPDn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dn', models.CharField(max_length=255, unique=True, validators=[helpers.validators.model_validators.validate_dn])),
            ],
        ),
        migrations.CreateModel(
            name='LDAPConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=255, unique=True, validators=[helpers.validators.model_validators.validate_hostname])),
                ('ldap_user', models.CharField(max_length=255, validators=[helpers.validators.model_validators.validate_username])),
                ('krb_auth', models.BooleanField(default=False)),
                ('ldap_password', models.CharField(blank=True, max_length=255, null=True)),
                ('dns_hostname', models.ManyToManyField(to='ldapconfig.dnshost')),
                ('group_dn', models.ManyToManyField(related_name='group_ldapconfig_set', to='ldapconfig.ldapdn')),
                ('user_dn', models.ManyToManyField(to='ldapconfig.ldapdn')),
            ],
        ),
    ]
