from django.shortcuts import render, redirect
from .models import Celular
from .forms import CelularFormulario, BuscarCelular
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio/index.html")


@login_required
def crear_celu(request):
    
    registro = CelularFormulario()
    
    if request.method == "POST":

        registro = CelularFormulario(request.POST)
        if registro.is_valid():
            a = registro.cleaned_data
            celular = Celular(fabricante=a.get("fabricante"), modelo=a.get("modelo"), color=a.get("color"), anio=a.get("anio"))
            celular.save()
            return redirect('crear_celu')
            
            
    return render(request, 'inicio/reg_celular.html', {'form': registro})


def buscar_celu(request):
    
    buscador = BuscarCelular(request.GET)
    
    if buscador.is_valid():
        
        modelo = buscador.cleaned_data.get('modelo')
        color = buscador.cleaned_data.get('color')
        fabricante = buscador.cleaned_data.get('fabricante')
        celulares = Celular.objects.filter(fabricante__icontains = fabricante, modelo__icontains = modelo, color__icontains = color)
    else:
        celulares = Celular.objects.all()
    
    return render(request, 'inicio/buscador.html', {'celulares': celulares, 'search': buscador})
    
    
    
def about(request):
    
    return render(request, 'inicio/about.html')
    
class Descripcion(DetailView):
    model = Celular
    template_name = "inicio/descripcion.html"

class Borrar(LoginRequiredMixin, DeleteView):
    model = Celular
    template_name = "inicio/borrar.html"
    success_url = reverse_lazy("buscar_celu")
    

class Editar(LoginRequiredMixin, UpdateView):
    model = Celular
    template_name = "inicio/editar.html"
    success_url = reverse_lazy('buscar_celu')
    fields = ['fabricante', 'modelo', 'color', 'anio', 'imagen']
