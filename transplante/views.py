from django.shortcuts import render
from .models import Paciente, Clinicos
from .forms import PacienteForm, ClinicosForm

# Create your views here.

def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	return render(request, 'transplante/lista_pacientes.html', {'pacientes': pacientes})


def lista_clinicos(request):
	clinicos = Clinicos.objects.all()
	return render(request, 'transplante/lista_clinicos.html', {'clinicos': clinicos})
