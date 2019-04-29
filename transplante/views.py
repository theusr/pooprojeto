from django.shortcuts import render
from .models import Paciente
from .forms import PacienteForm

# Create your views here.

def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	return render(request, 'transplante/lista_pacientes.html', {'pacientes': pacientes})

