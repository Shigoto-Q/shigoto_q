# Generated by Django 3.1.7 on 2022-05-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0027_auto_20220522_1404"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="active_ingress",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="total_active_deployments",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="total_active_namespaces",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="total_active_services",
            field=models.IntegerField(default=0),
        ),
    ]