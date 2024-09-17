from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    # Validación de que ambas contraseñas coincidan
    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        
        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return password_confirmation
    
    # Sobrescribir el método save para almacenar correctamente la contraseña
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Encriptar la contraseña
        
        if commit:
            user.save()
        
        return user
