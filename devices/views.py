from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from .models import Device
from .serializers import DeviceSerializer


class DevicesViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """Devices model view set."""

    filter_backends = (SearchFilter,)
    serializer_class = DeviceSerializer
    search_fields = ("name",)
    queryset = Device.objects.all()

    def get_queryset(self):
        return Device.objects.filter(active=True).filter_by_user(self.request.user).order_by("name")
