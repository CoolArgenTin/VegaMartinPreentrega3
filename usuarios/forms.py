from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), min_length=5)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput(), min_length=5)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}    
        
class Editar(UserChangeForm):
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    avatar = forms.ImageField(required=False, label='Avatar')
    bio = forms.CharField(required=False, label='Descripción')
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'bio']



    