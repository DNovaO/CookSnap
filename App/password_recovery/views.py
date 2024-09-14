from django.shortcuts import render

# Create your views here.

def password_recovery(request):
    return render(request, 'password_recovery_template/password_recovery.html')