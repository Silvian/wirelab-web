from rest_framework import serializers

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
