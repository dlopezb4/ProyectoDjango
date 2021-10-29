
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Estudiante
from .forms import EstudianteForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class PlanesView(TemplateView):
    template_name='planes.html'


class MostrarView(TemplateView):
    template_name='mostrar.html'

class ContactoView(TemplateView):
    template_name='contacto.html'


class LoginView(TemplateView):
    template_name='login.html'

class AgregarusuarioView(TemplateView):
    template_name='agregarusuario.html'

class ListarEstudiante(ListView):
    template_name ='listar_est.html'
    model = Estudiante

def get_queryset(self):
    return Estudiante.objects.all()


class CrearEstudianteView(CreateView):
    template_name = 'crear.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('home:crear')
