#/main/urls.py
from django.urls import path
from .views import main_view
from .views import saved_recipes
from .views import explore_recipes_view
from .views import groceries

urlpatterns = [
    path('', main_view, name='main'),

]