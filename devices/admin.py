from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

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
