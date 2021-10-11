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
        instance = super().update(instance, validated_data)
        update_device_status(instance.unique_id, instance.state)
        return instance
