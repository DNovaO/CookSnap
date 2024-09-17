from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

def password_recovery(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            # Envía el correo con el link de recuperación
            send_mail(
                'Recuperación de contraseña',
                'Aquí está el enlace para restablecer tu contraseña: https://www.youtube.com/?app=desktop&hl=es',
                'leo_mata7791@outlook.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Se ha enviado un correo para restablecer tu contraseña.')
        except User.DoesNotExist:
            messages.error(request, 'Este correo no está registrado.')
    return render(request, 'password_recovery_template/password_recovery.html')
