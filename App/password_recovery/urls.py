from django.urls import path
from . import views

urlpatterns = [
    path('', views.password_recovery, name='password_recovery'),
]
