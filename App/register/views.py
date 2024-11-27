from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # Validar contraseñas
        if password != password_confirmation:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Verificar si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "The username is already taken.")
            return redirect('register')

        # Verificar si el correo ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('register')

        # Crear usuario
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('login')  # Cambiar al nombre de la URL de tu página de inicio de sesión
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('register')
    return render(request, 'register_template/register.html')
