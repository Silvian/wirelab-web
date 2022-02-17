from unittest import mock
from django.test import TestCase

from devices.factories import DeviceFactory
from devices.models import DeviceState
from siri.factories import SiriConfigurationFactory, VoiceCommandFactory


class TestVoiceCommandsIntegrationTestCase(TestCase):

    def setUp(self):
        self.config = SiriConfigurationFactory()
        self.device = DeviceFactory()
        self.command_off = VoiceCommandFactory(device=self.device)
        self.command_on = VoiceCommandFactory(
            change_state=DeviceState.ON.value,
            device=self.device,
        )
        self.command_off_without_device = VoiceCommandFactory(device=None)
        self.command_on_without_device = VoiceCommandFactory(
            change_state=DeviceState.ON.value,
            device=None,
        )

    @mock.patch("siri.views.update_device_status")
    def test_valid_voice_on_command_specific_device(self, device_status):
        response = self.client.get(f"/siri/command/{str(self.command_on.unique_id)}/")
        device_status.assert_called_once_with(
            self.command_on.device.unique_id,
            self.command_on.change_state,
        )
        self.assertEqual(
            response.status_code,
            200,
        )

    @mock.patch("siri.views.update_device_status")
    def test_valid_voice_off_command_specific_device(self, device_status):
        response = self.client.get(f"/siri/command/{str(self.command_off.unique_id)}/")
        device_status.assert_called_once_with(
            self.command_off.device.unique_id,
            self.command_off.change_state,
        )
        self.assertEqual(
            response.status_code,
            200,
        )

    @mock.patch("siri.views.update_device_status")
    def test_valid_voice_on_command_no_device(self, device_status):
        response = self.client.get(f"/siri/command/{str(self.command_on_without_device.unique_id)}/")
        device_status.assert_called_once_with(
            self.device.unique_id,
            self.command_on_without_device.change_state,
        )
        self.assertEqual(
            response.status_code,
            200,
        )

    @mock.patch("siri.views.update_device_status")
    def test_valid_voice_off_command_no_device(self, device_status):
        response = self.client.get(f"/siri/command/{str(self.command_off_without_device.unique_id)}/")
        device_status.assert_called_once_with(
            self.device.unique_id,
            self.command_off_without_device.change_state,
        )
        self.assertEqual(
            response.status_code,
            200,
        )

    def test_invalid_voice_command(self):
        response = self.client.get(f"/siri/command/f234f579-4124-4e47-81c6-29f4b6173653/")
        self.assertEqual(
            response.status_code,
            404,
        )

    def test_siri_config_disabled(self):
        self.config.enabled = False
        self.config.save()
        self.config.refresh_from_db()

        response = self.client.get(f"/siri/command/{str(self.command_on.unique_id)}/")
        self.assertEqual(
            response.status_code,
            404,
        )
