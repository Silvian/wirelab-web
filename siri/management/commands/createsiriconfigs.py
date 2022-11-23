"""Command to create the default siri configs."""

from django.core.management import BaseCommand

from services.utils import RandomHashGenerator
from siri.models import SiriConfiguration


class Command(BaseCommand):
    """Create the default siri configs when building the application for the first time."""

    help = __doc__

    def handle(self, *args, **options):
        """Create default siri configuration."""
        config = SiriConfiguration.load()
        generator = RandomHashGenerator()
        if not config:
            config = SiriConfiguration.objects.create(
                name="Siri voice commands",
                api_key=generator.generate_hash(),
                enabled=True,
            )
            self.stdout.write(self.style.SUCCESS(
                "Successfully created: %s" % config.name)
            )

        else:
            if config.api_key == "secret key":
                config.api_key = generator.generate_hash()
                config.save()
                self.stdout.write(self.style.SUCCESS(
                    "%s api key created" % config.name)
                )
            else:
                self.stdout.write(self.style.WARNING(
                    "%s already exists" % config.name)
                )
