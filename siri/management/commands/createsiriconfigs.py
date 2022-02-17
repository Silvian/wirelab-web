"""Command to create the default siri configs."""

from django.core.management import BaseCommand

from siri.models import SiriConfiguration


class Command(BaseCommand):
    """Create the default siri configs when building the application for the first time."""

    help = __doc__

    def handle(self, *args, **options):
        """Create default siri configuration."""
        config = SiriConfiguration.load()
        if not config:
            config = SiriConfiguration.objects.create(
                name="Siri voice commands",
                enabled=True,
            )
            self.stdout.write(self.style.SUCCESS(
                "Successfully created: %s" % config.name)
            )

        else:
            self.stdout.write(self.style.WARNING(
                "%s already exists" % config.name)
            )
