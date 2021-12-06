import factory
from factory import faker

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    """User Model Factory."""

    class Meta:
        model = User

    email = faker.Faker("email")
    first_name = faker.Faker("first_name")
    last_name = faker.Faker("last_name")
    country = faker.Faker("country")
    mobile = faker.Faker("phone_number")
    active = True
    staff = False
    admin = False


class StaffUserFactory(UserFactory):
    """Staff User Model Factory."""

    staff = True


class AdminUserFactory(StaffUserFactory):
    """Admin User Model Factory."""

    admin = True
