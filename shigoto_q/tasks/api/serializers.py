import datetime

from django_celery_beat.models import (
    ClockedSchedule,
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
    SolarSchedule,
)
from rest_framework import serializers
from rest_framework.fields import Field


class TimezoneField(Field):
    """
    Serializing TimeZoneFild
    """

    def to_representation(self, obj):
        return obj.zone

    def to_internal_value(self, data):
        return data


class CrontabSerializer(serializers.ModelSerializer):
    timezone = TimezoneField()

    class Meta:
        model = CrontabSchedule
        fields = [
            "id",
            "minute",
            "hour",
            "day_of_month",
            "month_of_year",
            "day_of_week",
            "timezone",
        ]


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = ["every", "period"]


class ClockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockedSchedule
        fields = ["clocked_time"]


class SolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarSchedule
        fields = ["event", "latitude", "longitude"]


class TaskGetSerializer(serializers.ModelSerializer):
    crontab = CrontabSerializer()

    class Meta:
        model = PeriodicTask
        fields = [
            "name",
            "task",
            "crontab",
            "interval",
            "clocked",
            "solar",
            "args",
            "kwargs",
            "queue",
            "exchange",
            "routing_key",
            "headers",
            "priority",
            "expires",
            "expire_seconds",
            "one_off",
            "start_time",
            "enabled",
            "last_run_at",
            "total_run_count",
            "date_changed",
            "description",
        ]


class TaskPostSerializer(serializers.ModelSerializer):
    task = serializers.SerializerMethodField(read_only=True)

    def get_task(self, obj):
        return getattr(obj, "task", "shigoto_q.tasks.tasks.custom_endpoint")

    class Meta:
        model = PeriodicTask
        fields = [
            "name",
            "task",
            "crontab",
            "interval",
            "clocked",
            "solar",
            "args",
            "kwargs",
            "queue",
            "priority",
            "expires",
            "expire_seconds",
            "one_off",
            "enabled",
        ]

    def create(self, validated_data):
        task_created = PeriodicTask.objects.create(
            task="shigoto_q.tasks.tasks.custom_endpoint",
            crontab=validated_data["crontab"],
            interval=validated_data["interval"],
            clocked=validated_data["clocked"],
            solar=validated_data["solar"],
            name=validated_data["name"],
            kwargs=validated_data["kwargs"],
            args=validated_data["args"],
            queue=validated_data["queue"],
            priority=validated_data["priority"],
            expires=validated_data["expires"],
            expire_seconds=validated_data["expire_seconds"],
            one_off=validated_data["one_off"],
            enabled=validated_data["enabled"],
        )
        self.context["request"].user.task.add(task_created)
        return task_created
