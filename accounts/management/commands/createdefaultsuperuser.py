"""Command to create default super user."""

from django.core.management import BaseCommand
from django.conf import settings

from accounts.models import User


class Command(BaseCommand):
    """Create a default super user when building the application for the first time."""

    help = __doc__

    def handle(self, *args, **options):
        """Create default super user."""
        if not User.objects.filter(email=settings.DEFAULT_SUPER_USER).exists():
            user = User.objects.create_superuser(
                email=settings.DEFAULT_SUPER_USER,
                password=settings.DEFAULT_SUPER_USER_PASSWORD,
            )
            self.stdout.write(self.style.SUCCESS(
                "Default super user created: %s" % user.email)
            )

        else:
            self.stdout.write(self.style.WARNING(
                "Default super user already exists")
            )
