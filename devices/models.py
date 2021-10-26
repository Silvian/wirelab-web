import uuid
from django.db import models

from devices.managers import DeviceManager
from wirelab.base_enums import ChoiceEnum
from wirelab.base_models import TimeStampedModel


class DeviceState(ChoiceEnum):
    ON = "On"
    OFF = "Off"


class Device(TimeStampedModel):
    """Device model."""

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
        primary_key=True,
    )
    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=10,
        choices=DeviceState.choices(),
    )
    auto = models.BooleanField(
        default=False,
        help_text="Based on sunset times"
    )
    delay = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Auto delay time in minutes",
    )
    active = models.BooleanField(
        default=True,
    )
    owners = models.ManyToManyField(
        "accounts.User",
        related_name="devices",
        blank=True,
    )

    objects = DeviceManager()

    def __str__(self):
        return self.name
