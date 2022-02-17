from django.urls import path

from . import views

app_name = "siri"

urlpatterns = [
    path('command/<uuid:unique_id>/', views.voice_commands, name='voice_command'),
]
