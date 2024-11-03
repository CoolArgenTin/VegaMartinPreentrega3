from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import Registro, Editar
from .models import DatosExtra
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin


def loguear(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():

            user1 = formulario.get_user()
            
            login(request, user1)
            
            DatosExtra.objects.get_or_create(user=user1)
            
            return redirect('inicio')
            
    
    return render(request, 'usuarios/login.html', {'form': formulario})


def registrar(request):
    
    formulario = Registro()
    
    if request.method == 'POST':
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': formulario})


def perfil(request):
    
    return render(request, 'usuarios/perfil.html')

@login_required
def editarperfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = Editar(instance=request.user, initial={'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = Editar(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            
            datos_extra.save()
            
            desc = formulario.cleaned_data.get('bio')
            
            datos_extra.bio = desc if desc else datos_extra.bio
            
            datos_extra.save()
            
            formulario.save()
            
            
            return redirect('usuarios:perfil')
    
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})


class CambiarPassword(PasswordChangeView):
    
    template_name = 'usuarios/cambiar_contra.html'
    
    success_url = reverse_lazy('usuarios:editar_perfil')


class Borrar(SuccessMessageMixin, DeleteView):
    model = User
    template_name = "usuarios/borrar.html"
    success_message = "El usuario ha sido eliminado"
    success_url = reverse_lazy("inicio")