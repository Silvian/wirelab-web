import uuid

from rest_framework import serializers

from devices.models import DeviceState


class SiriSerializer(serializers.Serializer):
    """Siri Serializer."""

    device_name = serializers.CharField(
        required=False,
        max_length=200,
        allow_null=True,
        allow_blank=True,
    )
    state = serializers.ChoiceField(
        required=True,
        choices=DeviceState.choices(),
    )


class WebhookSerializer(serializers.Serializer):
    """Webhook Serializer."""

    unique_id = serializers.UUIDField(
        default=uuid.uuid4(),
    )
    active = serializers.BooleanField(
        required=False,
        allow_null=True,
    )
    state = serializers.ChoiceField(
        required=False,
        allow_null=True,
        allow_blank=True,
        choices=DeviceState.choices(),
    )
    auto = serializers.BooleanField(
        required=False,
        allow_null=True,
    )
