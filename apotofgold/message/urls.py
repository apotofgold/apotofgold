from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "message-home"),
    path('/about/', views.about, name = "message-about"),
]