from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
]
