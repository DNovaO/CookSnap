from django.urls import path
from .views import photo
urlpatterns = [
    path('photo/', photo, name='photo'),
]
