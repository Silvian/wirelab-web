from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "services"

router = DefaultRouter()

router.register(r"list-devices", views.ListDevicesViewSet, basename="devices")

urlpatterns = router.urls
urlpatterns += [
    path('siri/', views.SiriAPIView.as_view(), name='siri'),
    path('webhook/', views.WebhookAPIView.as_view(), name='webhook'),
]
