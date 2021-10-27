import uuid

from rest_framework import serializers


class WebhookSerializer(serializers.Serializer):
    """Webhook Serializer."""

    unique_id = serializers.UUIDField(
        default=uuid.uuid4(),
    )
    active = serializers.BooleanField(
        required=False,
        allow_null=True,
    )
    state = serializers.CharField(
        required=False,
        max_length=10,
        allow_null=True,
        allow_blank=True,
    )
