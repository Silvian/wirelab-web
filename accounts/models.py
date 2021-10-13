from django.db import models

from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django_countries.fields import CountryField

from wirelab.base_models import TimeStampedModel
from .managers import UserManager


class User(TimeStampedModel, AbstractBaseUser):
    """User account model."""

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    country = CountryField(
        blank=True,
        null=True,
    )
    mobile = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        default=True,
    )
    staff = models.BooleanField(
        default=False,
    )
    admin = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.email

    def get_short_name(self):
        if self.first_name:
            return self.first_name

        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email


class WebhookUser(AnonymousUser):

    @property
    def is_authenticated(self):
        # Always return True. This is a way to tell if
        # the user has been authenticated in permissions
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, module):
        return True

    def __str__(self):
        return "Webhook Anonymous User"
