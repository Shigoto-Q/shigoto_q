# Generated by Django 3.1.7 on 2021-04-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('users', '0005_user_crontab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='crontab',
        ),
        migrations.AddField(
            model_name='user',
            name='crontab',
            field=models.ManyToManyField(null=True, to='django_celery_beat.CrontabSchedule'),
        ),
    ]
