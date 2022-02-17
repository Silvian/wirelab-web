from django.db.models import Manager

from .queryset import DevicesQuerySet


class DeviceManager(Manager.from_queryset(DevicesQuerySet)):
    """Device manager."""
    pass
