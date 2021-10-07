from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'email',
        'first_name',
        'last_name',
        'country',
        'mobile',
        'admin',
    )

    readonly_fields = (
        'created',
        'modified',
    )

    list_filter = (
        'admin',
        'staff',
        'active',
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'country', 'mobile',)
        }),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
        ('Additional Info', {'fields': ('created', 'modified',)})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'country',
                'mobile',
            )
        }),
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
    )
    ordering = ('email',)
    filter_horizontal = ()
