from rest_framework import status
from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from devices.factories import DeviceFactory

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

