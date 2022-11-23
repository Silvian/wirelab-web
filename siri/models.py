import uuid
from django.db import models

from accounts.models import User
from devices.models import Device, DeviceState
from wirelab.base_models import SingletonModel, TimeStampedModel


class SiriConfiguration(SingletonModel):
    name = models.CharField(
        max_length=50,
        default='Siri voice commands'
    )
    api_key = models.CharField(
        max_length=255,
        default='secret key'
    )
    enabled = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name


class VoiceCommand(TimeStampedModel):
    """Voice command model."""

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
        primary_key=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    change_state = models.CharField(
        max_length=10,
        choices=DeviceState.choices(),
    )
    device = models.ForeignKey(
        Device,
        null=True,
        blank=True,
        related_name="voice_command",
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        User,
        related_name="voice_command",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return str(self.unique_id)
