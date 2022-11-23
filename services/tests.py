from unittest import mock
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from devices.factories import DeviceFactory
from siri.factories import SiriConfigurationFactory

from .factories import WebhookConfigurationFactory


class ListDevicesViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.webhook_config = WebhookConfigurationFactory()
        self.device = DeviceFactory()

    def test_list_devices(self):
        self.client.force_authenticate(user=self.user)
        url = "/api/v1/services/list-devices/"
        headers = {"X-API-KEY": self.webhook_config.api_key}

        response = self.client.get(url, **headers)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["unique_id"], str(self.device.unique_id))
        self.assertEqual(data[0]["state"], self.device.state)


class SiriAPIViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.config = SiriConfigurationFactory()
        self.device = DeviceFactory()
        self.url = "/api/v1/services/siri/"
        self.headers = {"X-API-KEY": self.config.api_key}

    @mock.patch("services.views.update_device_status")
    def test_all_devices_on_command(self, device_status):
        self.client.force_authenticate(user=self.user)
        data = {"state": "ON"}
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        device_status.assert_called_once_with(
            self.device.unique_id,
            "ON",
        )

    @mock.patch("services.views.update_device_status")
    def test_all_devices_off_command(self, device_status):
        self.client.force_authenticate(user=self.user)
        data = {"state": "OFF"}
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        device_status.assert_called_once_with(
            self.device.unique_id,
            "OFF",
        )

    @mock.patch("services.views.update_device_status")
    def test_specific_device_on_command(self, device_status):
        self.client.force_authenticate(user=self.user)
        data = {
            "device_name": self.device.name,
            "state": "ON",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        device_status.assert_called_once_with(
            self.device.unique_id,
            "ON",
        )

    @mock.patch("services.views.update_device_status")
    def test_specific_device_off_command(self, device_status):
        self.client.force_authenticate(user=self.user)
        data = {
            "device_name": self.device.name,
            "state": "OFF",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        device_status.assert_called_once_with(
            self.device.unique_id,
            "OFF",
        )

    def test_invalid_device_command(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "device_name": "Bob",
            "state": "ON",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_invalid_state_command(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "device_name": self.device.name,
            "state": "FOO",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_no_devices_available(self):
        self.device.active = False
        self.device.save()
        self.device.refresh_from_db()

        self.client.force_authenticate(user=self.user)
        data = {"state": "OFF"}
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_no_specific_device_available(self):
        self.device.active = False
        self.device.save()
        self.device.refresh_from_db()

        self.client.force_authenticate(user=self.user)
        data = {
            "device_name": self.device.name,
            "state": "ON",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )


class WebhookAPIViewTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.webhook_config = WebhookConfigurationFactory()
        self.device = DeviceFactory()
        self.url = "/api/v1/services/webhook/"
        self.headers = {"X-API-KEY": self.webhook_config.api_key}

    def test_update_active(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "unique_id": self.device.unique_id,
            "active": False,
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        self.device.refresh_from_db()
        self.assertEqual(
            self.device.active,
            False,
        )

    def test_update_state(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "unique_id": self.device.unique_id,
            "state": "ON",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        self.device.refresh_from_db()
        self.assertEqual(
            self.device.state,
            "ON",
        )

    def test_update_auto(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "unique_id": self.device.unique_id,
            "auto": True,
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            200,
        )
        self.device.refresh_from_db()
        self.assertEqual(
            self.device.auto,
            True,
        )

    def test_update_invalid_device(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "unique_id": "f234f579-4124-4e47-81c6-29f4b6173653",
            "state": "ON",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )

    def test_update_invalid_state(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "unique_id": self.device.unique_id,
            "state": "FOO",
        }
        response = self.client.post(self.url, **self.headers, data=data)
        self.assertEqual(
            response.status_code,
            400,
        )
