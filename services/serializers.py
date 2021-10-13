import uuid

from rest_framework import serializers


class WebhookSerializer(serializers.Serializer):
    unique_id = serializers.UUIDField(default=uuid.uuid4())
    active = serializers.BooleanField()
