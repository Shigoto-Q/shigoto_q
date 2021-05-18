# Generated by Django 3.1.7 on 2021-05-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_taskresult_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='task_beat_id',
            field=models.IntegerField(help_text='Celery beat (periodic task) ID', null=True, verbose_name='Celery beat ID'),
        ),
    ]
