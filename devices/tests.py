from unittest import mock

from rest_framework import status
from rest_framework.test import APITestCase

from accounts.factories import UserFactory
from devices.factories import DeviceFactory


class DevicesViewSetTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.device = DeviceFactory(owners=[self.user])
        self.device_2 = DeviceFactory()

    def test_list_devices(self):
        self.client.force_authenticate(user=self.user)
        url = "/api/v1/devices/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["unique_id"], str(self.device.unique_id))
        self.assertEqual(data[0]["state"], self.device.state)

    def test_get_device(self):
        self.client.force_authenticate(user=self.user)
        url = f"/api/v1/devices/{str(self.device.unique_id)}/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = response.json()
        self.assertEqual(data["unique_id"], str(self.device.unique_id))
        self.assertEqual(data["state"], self.device.state)

    @mock.patch("devices.serializers.update_device_status")
    def test_device_state_update(self, _):
        self.client.force_authenticate(user=self.user)
        url = f"/api/v1/devices/{str(self.device.unique_id)}/"
        data = {"state": "ON"}
        response = self.client.patch(url, data=data)
        self.device.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.device.state, "ON")

    def test_device_enable_auto(self):
        self.client.force_authenticate(user=self.user)
        url = f"/api/v1/devices/{str(self.device.unique_id)}/"
        data = {"auto": True}
        response = self.client.patch(url, data=data)
        self.device.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.device.active)

    def test_device_enable_auto_with_delay(self):
        self.client.force_authenticate(user=self.user)
        url = f"/api/v1/devices/{str(self.device.unique_id)}/"
        data = {
            "auto": True,
            "delay": 30,
        }
        response = self.client.patch(url, data=data)
        self.device.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTrue(self.device.active)
        self.assertEqual(self.device.delay, 30)

    def test_device_unauthenticated(self):
        url = f"/api/v1/devices/{str(self.device.unique_id)}/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_devices_not_owned(self):
        self.client.force_authenticate(user=self.user)
        url = f"/api/v1/devices/{str(self.device_2.unique_id)}/"
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
