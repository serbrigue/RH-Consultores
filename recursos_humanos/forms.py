from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    correo = forms.EmailField(label='Correo electrónico', required=True)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea, required=True)


