"""tes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import  HomeView ,PlanesView,AgregarusuarioView,ListarEstudiante,CrearEstudianteView,MostrarView,ContactoView,LoginView

app_name='home'
urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
    path('planes/', PlanesView.as_view(), name='planes'),
    path('mostrar/', MostrarView.as_view(), name='mostrar'),
    path('agregarusuario/', AgregarusuarioView.as_view(), name='agregarusuario'),
    path('listest/', ListarEstudiante.as_view(), name='listar_est'),
    path('crear/', CrearEstudianteView.as_view(), name='crear'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('login/', LoginView.as_view(), name='login'),
    
 ]
    