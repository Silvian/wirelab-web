from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        'unique_id',
        'name',
        'state',
        'active',
        'created',
    )

    list_filter = (
        'state',
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
