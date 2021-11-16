from rest_framework import serializers

from services.utils import update_device_status
from . models import Device


class DeviceSerializer(serializers.ModelSerializer):
    """Device model serializer."""

    class Meta:
        model = Device
        fields = (
            "unique_id",
            "name",
            "description",
            "state",
            "auto",
            "delay",
            "active",
            "created",
            "modified",
        )

        read_only_fields = (
            "unique_id",
            "name",
            "description",
            "active",
            "created",
            "modified",
        )

    def update(self, instance, validated_data):
        device = Device.objects.get(unique_id=instance.unique_id)
        instance = super().update(instance, validated_data)
        if device.state != instance.state:
            update_device_status(instance.unique_id, instance.state)
        return instance
