from django.urls import path, include

app_name = "api-v1"

urlpatterns = [
    path("devices/", include("devices.api_urls", namespace="devices")),
]
