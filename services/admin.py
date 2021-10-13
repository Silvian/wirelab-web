from django.contrib import admin

from . models import WebhookConfiguration


@admin.register(WebhookConfiguration)
class WebhookConfigurationAdmin(admin.ModelAdmin):
    """WebhookConfiguration admin."""

    list_display = (
        'name',
        'api_key',
        'enabled',
    )
