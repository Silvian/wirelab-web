from django.contrib import admin

from . models import SiriConfiguration, VoiceCommand


@admin.register(SiriConfiguration)
class SiriConfigurationAdmin(admin.ModelAdmin):
    """SiriConfiguration admin."""

    list_display = (
        'name',
        'enabled',
    )


@admin.register(VoiceCommand)
class VoiceCommandAdmin(admin.ModelAdmin):
    """VoiceCommand admin."""

    list_display = (
        'unique_id',
        'description',
        'change_state',
    )

    list_filter = (
        'change_state',
    )

    readonly_fields = (
        'unique_id',
        'created',
        'modified',
    )

    search_fields = (
        'name',
        'change_state',
        'device',
    )
