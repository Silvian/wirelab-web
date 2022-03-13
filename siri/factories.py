import factory
from factory import faker

from accounts.factories import UserFactory
from devices.factories import DeviceFactory
from devices.models import DeviceState
from .models import SiriConfiguration, VoiceCommand


class SiriConfigurationFactory(factory.django.DjangoModelFactory):
    """Siri Configuration Model Factory."""

    class Meta:
        model = SiriConfiguration

    name = "Siri voice commands"
    enabled = True


class VoiceCommandFactory(factory.django.DjangoModelFactory):
    """Voice Command Model Factory."""

    class Meta:
        model = VoiceCommand

    description = faker.Faker("sentence")
    change_state = DeviceState.OFF.value
    device = factory.SubFactory(DeviceFactory)
    user = factory.SubFactory(UserFactory)
