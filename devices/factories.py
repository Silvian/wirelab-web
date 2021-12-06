import factory
from factory import faker

from .models import Device, DeviceState


class DeviceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Device

    name = faker.Faker("name")
    description = faker.Faker("sentence")
    state = DeviceState.OFF.value
    auto = False
    delay = 0
    active = True

    @factory.post_generation
    def owners(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for owner in extracted:
                self.owners.add(owner)
