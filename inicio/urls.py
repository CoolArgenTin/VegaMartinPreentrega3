from django.urls import path
from inicio.views import inicio, crear_celu, buscar_celu, about

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reg-celular/', crear_celu, name='crear_celu'),
    path('buscador/', buscar_celu, name='buscar_celu'),
    path('about-me/', about, name='about')
]
