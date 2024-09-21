# password_recovery/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.password_recovery, name='password_recovery'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_change_template/password_change.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_change_template/password_change_done.html"), name='password_reset_complete'),

    # URL para cambiar la contraseña
    path('change/', auth_views.PasswordChangeView.as_view(template_name="password_change_template/password_change.html"), name='password_change'),

    # URL para confirmar que la contraseña fue cambiada
    path('change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_template/password_change_done.html"), name='password_change_done'),
]
