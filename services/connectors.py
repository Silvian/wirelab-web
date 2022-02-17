import requests

from django.conf import settings


class DeviceServiceConnector:
    """Device Service Connector."""

    def __init__(
            self,
            service_url=settings.DEVICE_SERVICE_URL,
            api_key=settings.DEVICE_SERVICE_API_KEY,
    ):
        self.service_url = service_url
        self.api_key = api_key

    def state_update(self, unique_id, state):
        """Send State Update Message."""
        response = requests.post(
            url=self.service_url,
            headers={
                'Content-Type': 'application/json',
                'x-api-key': self.api_key,
            },
            json={
                'device_id': str(unique_id),
                'state': state,
            }
        ).json()

        return response
