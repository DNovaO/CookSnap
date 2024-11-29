"""
version 1.0 - 22/11/2024 - Aguilar Velázquez Marco Antonio:
    Inicia un método de vista que permite a los usuarios iniciar su cámara en la aplicación.
    Direccioa al apartado de la cámara para que el usuario pueda capturar diferente información.
"""
from django.shortcuts import render

def photo(request):
    return render(request, 'photoTemplate\photoTemplate.html')