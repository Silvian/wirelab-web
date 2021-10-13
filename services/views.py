from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Device
from .authentication import CsrfExemptSessionAuthentication, WebhookAuthentication
from . serializers import WebhookSerializer


class WebhookAPIView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, WebhookAuthentication)

    def post(self, request):
        serializer = WebhookSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            device = Device.objects.filter(unique_id=data["unique_id"]).first()
            if device:
                device.active = data["active"]
                device.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Device.objects.all()
