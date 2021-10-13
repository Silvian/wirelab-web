import hashlib
import random
import time

from django.conf import settings

from . connectors import DeviceServiceConnector


def update_device_status(unique_id, state):
    connector = DeviceServiceConnector()
    connector.state_update(unique_id, state)


class RandomHashGenerator:
    """Unique random hash generator."""

    def __init__(self, salt=settings.SECRET_KEY):
        self.salt = salt

    def generate_hash(self):
        """Generate random hash based on secure random and time."""
        random_bits = random.getrandbits(256)
        unique_time = time.time()
        random_string = self.salt + str(random_bits) + str(unique_time)
        h = hashlib.sha256()
        encoded_string = random_string.encode("utf-8")
        h.update(encoded_string)
        return h.hexdigest()
