from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    actions = (
        'enable_auto',
        'disable_auto',
    )

    list_display = (
        'name',
        'state',
        'auto',
        'active',
    )

    list_filter = (
        'state',
        'auto',
        'active',
    )

    readonly_fields = (
        'unique_id',
        'created',
        'modified',
    )

    search_fields = (
        'name',
        'state',
        'owners',
    )

    filter_horizontal = (
        'owners',
    )

    @admin.action(description='Enable auto for selected devices')
    def enable_auto(self, request, queryset):
        enabled = queryset.update(auto=True)
        self.message_user(request, ngettext(
            'Enabled auto mode based on sunset for %d device.',
            'Enabled auto mode based on sunset for %d devices.',
            enabled,
        ) % enabled, messages.SUCCESS)

    @admin.action(description='Disable auto for selected devices')
    def disable_auto(self, request, queryset):
        disabled = queryset.update(auto=False)
        self.message_user(request, ngettext(
            'Disabled auto mode based on sunset for %d device.',
            'Disabled auto mode based on sunset for %d devices.',
            disabled,
        ) % disabled, messages.SUCCESS)
