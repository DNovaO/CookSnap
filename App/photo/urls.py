from django.urls import path
from .views import photo_view
urlpatterns = [
    path('', photo_view, name='photo'),
]

