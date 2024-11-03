from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reg-celular/', views.crear_celu, name='crear_celu'),
    path('about-me/', views.about, name='about'),
    path('buscador/', views.buscar_celu, name='buscar_celu'),
    path('buscador/<int:pk>', views.Descripcion.as_view(), name='descripcion'),
    path('buscador/<int:pk>/borrar', views.Borrar.as_view(), name='borrar'),
    path('buscador/<int:pk>/editar', views.Editar.as_view(), name='editar_celu'),
]
