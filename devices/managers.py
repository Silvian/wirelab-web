from django.db.models import Manager

from .queryset import DevicesQuerySet


class DeviceManager(Manager.from_queryset(DevicesQuerySet)):
    """Payload setup manager."""
    pass
