from django.shortcuts import render, redirect
from .forms import RegisterForm  # Importa el formulario

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # O la ruta a la que quieras redirigir después del registro
    else:
        form = RegisterForm()
    
    return render(request, 'register_template/register.html', {'form': form})
