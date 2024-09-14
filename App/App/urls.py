#app/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('main/', include('main.urls')),
    path('explore_recipes/', include('explore_recipes.urls')),
    path('saved_recipes/', include('saved_recipes.urls')),
    path('groceries/', include('groceries.urls')),
    path('password_recovery/', include('password_recovery.urls')),


]
