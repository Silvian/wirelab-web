from rest_framework import authentication

from accounts.models import WebhookUser
from services.models import WebhookConfiguration


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class WebhookAuthentication(authentication.BaseAuthentication):
    """Custom webhook authentication class."""

    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")
        config = WebhookConfiguration.load()
        if config.enabled:
            if api_key == config.api_key:
                user = WebhookUser()
                return user, None

        return None
