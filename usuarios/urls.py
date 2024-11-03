from django.urls import path 
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.loguear, name='login'),
    path('logout/', LogoutView.as_view(template_name='inicio/index.html'), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editarperfil, name='editar_perfil'),
    path('perfil/editar/contra', views.CambiarPassword.as_view(), name='cambiar_contra'),
    path('perfil/eliminar/<int:pk>', views.Borrar.as_view(template_name='usuarios/borrar.html'), name='borrar')
]
