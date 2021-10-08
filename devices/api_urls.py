from rest_framework.routers import DefaultRouter

from .views import DevicesVewSet

app_name = "devices"

router = DefaultRouter()

router.register(r"", DevicesVewSet, basename="devices")

urlpatterns = router.urls
