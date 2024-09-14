from django.urls import path
from . import views

urlpatterns = [
    path('', views.groceries, name='groceries'),
]
