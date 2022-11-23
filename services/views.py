from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from devices.models import Device
from devices.serializers import DeviceSerializer
from .authentication import CsrfExemptSessionAuthentication, SiriAuthentication, WebhookAuthentication
from .serializers import SiriSerializer, WebhookSerializer
from .utils import update_device_status


class SiriAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, SiriAuthentication)

    def post(self, request):
        serializer = SiriSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            device_name = data.get("device_name")
            if device_name:
                device = Device.objects.filter(name=device_name, active=True).first()
                if device:
                    update_device_status(device.unique_id, data["state"])
                    return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                devices = Device.objects.filter(active=True)
                if devices:
                    for device in devices:
                        update_device_status(device.unique_id, data["state"])

                    return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Device.objects.all()


class WebhookAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, WebhookAuthentication)

    def post(self, request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            device = Device.objects.filter(unique_id=data["unique_id"]).first()
            if device:
                active = data.get("active")
                state = data.get("state")
                auto = data.get("auto")
                if active is not None:
                    device.active = active
                if state is not None:
                    device.state = state
                if auto is not None:
                    device.auto = auto
                device.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Device.objects.all()


class ListDevicesViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    authentication_classes = (CsrfExemptSessionAuthentication, WebhookAuthentication)
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    def get_queryset(self):
        return Device.objects.filter(active=True)
