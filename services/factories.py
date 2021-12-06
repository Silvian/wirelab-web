import factory

from .models import WebhookConfiguration


class WebhookConfigurationFactory(factory.django.DjangoModelFactory):
    """Webhook Configuration Model Factory."""

    class Meta:
        model = WebhookConfiguration

    name = "Webhook configuration"
    api_key = "test_key"
    enabled = True
