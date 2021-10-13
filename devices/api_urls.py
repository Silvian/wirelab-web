from rest_framework.routers import DefaultRouter

from . import views

app_name = "devices"

router = DefaultRouter()

router.register(r"", views.DevicesViewSet, basename="devices")

urlpatterns = router.urls
