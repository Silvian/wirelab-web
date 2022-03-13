from django.http import HttpResponse

from devices.models import Device
from services.utils import update_device_status
from . models import SiriConfiguration, VoiceCommand


def voice_commands(request, unique_id):
    if request.method == 'GET':
        config = SiriConfiguration.load()
        if not config.enabled:
            return HttpResponse(status=404)

        try:
            command = VoiceCommand.objects.get(unique_id=unique_id)
            if command.device:
                if command.device.active:
                    update_device_status(command.device.unique_id, command.change_state)

            else:
                devices = Device.objects.filter(active=True).filter_by_user(command.user)
                for device in devices:
                    update_device_status(device.unique_id, command.change_state)

        except VoiceCommand.DoesNotExist:
            return HttpResponse(status=404)

        return HttpResponse(status=200)
