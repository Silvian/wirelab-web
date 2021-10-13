from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('webhook/', views.WebhookAPIView.as_view(), name='webhook'),
]
