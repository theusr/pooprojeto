from django.shortcuts import render, get_object_or_404
from .models import Paciente, Clinico, Secretario
from .forms import PacienteForm, ClinicoForm, SecretarioForm

# Create your views here.

def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	clinicos = Clinico.objects.all()
	secretarios = Secretario.objects.all()
	return render(request, 'transplante/lista_pacientes.html', {'secretarios': secretarios})


def lista_clinicos(request):
	clinicos = Clinico.objects.all()
	return render(request, 'transplante/lista_pacientes.html', {'clinicos': clinicos})

def lista_secretarios(request):
	secretarios = Secretario.object.all()
	return render(request, 'transplante/lista_secretarios.html', {'secretarios': secretarios})

def paciente_detail(request, pk):
    post = get_object_or_404(Paciente, pk=pk)
    return render(request, 'transplante/paciente_detail.html', {'pacientes': pacientes})

def clinico_detail(request, pk):
    post = get_object_or_404(Clinico, pk=pk)
    return render(request, 'transplante/clinico_detail.html', {'clinicos': clinicos})

def secretario_detail(request, pk):
    post = get_object_or_404(Secretario, pk=pk)
    return render(request, 'transplante/secretario_detail.html', {'secretarios': secretarios})
