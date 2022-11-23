"""Command to create default configs."""

from django.core.management import BaseCommand

from services.models import WebhookConfiguration
from services.utils import RandomHashGenerator


class Command(BaseCommand):
    """Create a default superuser when building the application for the first time."""

    help = __doc__

    def handle(self, *args, **options):
        """Create default services webhook configuration."""
        config = WebhookConfiguration.load()
        generator = RandomHashGenerator()
        if not config:
            config = WebhookConfiguration.objects.create(
                name="Webhook configuration",
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
