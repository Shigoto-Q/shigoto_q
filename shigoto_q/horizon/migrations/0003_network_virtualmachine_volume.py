# Generated by Django 3.1.7 on 2022-10-01 17:24

import common.db.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('horizon', '0002_auto_20221001_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('interface_id', models.CharField(max_length=512, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=512)),
                ('availability_zone', models.CharField(choices=[('eu-central-1a', 'Eu Central 1A'), ('eu-central-1b', 'Eu Central 1B')], max_length=512)),
                ('public_ipv4_dns', models.CharField(max_length=512, null=True)),
                ('public_ipv4_address', models.CharField(max_length=512, null=True)),
                ('private_ipv4_dns', common.db.fields.EncryptedCharField(null=True)),
                ('private_ipv4_address', common.db.fields.EncryptedCharField(null=True)),
                ('public_ipv6_address', models.CharField(max_length=512, null=True)),
                ('vpc_id', common.db.fields.EncryptedCharField()),
                ('subnet_id', common.db.fields.EncryptedCharField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.CharField(max_length=512, primary_key=True, serialize=False, unique=True)),
                ('device_name', models.CharField(max_length=512)),
                ('attachment_status', models.PositiveSmallIntegerField(choices=[(0, 'Attached')])),
                ('attachment_time', models.DateTimeField()),
                ('encrypted', models.BooleanField(default=False)),
                ('size', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('instance_id', models.CharField(max_length=512, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=512)),
                ('operating_system', models.PositiveSmallIntegerField(choices=[(0, 'Ubuntu'), (1, 'Debian'), (2, 'Windows')])),
                ('type', models.PositiveIntegerField(choices=[(0, 'Micro')])),
                ('state', models.PositiveSmallIntegerField(choices=[(0, 'Starting'), (1, 'Running')])),
                ('launch_time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='horizon.network')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='horizon.volume')),
            ],
        ),
    ]
