# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("¡Hola, mundo! esta es la página de login.")