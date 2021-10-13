from django.db import models

from wirelab.base_models import SingletonModel


class WebhookConfiguration(SingletonModel):
    name = models.CharField(
        max_length=50,
        default='Webhook configuration'
    )
    api_key = models.CharField(
        max_length=255,
        default='secret key'
    )
    enabled = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name
