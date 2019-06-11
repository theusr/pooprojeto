from django.shortcuts import render, get_object_or_404
from .models import Paciente, Clinico, Secretario
from .forms import PacienteForm, ClinicoForm, SecretarioForm

# Create your views here.

def home(request):
	return render (request, 'transplante/home.html', {'home': home})

def lista_pacientes(request):
	pacientes = Paciente.objects.all()
	clinicos = Clinico.objects.all()
	secretarios = Secretario.objects.all()
	return render(request, 'transplante/lista_pacientes.html', {'pacientes': pacientes, 'clinicos': clinicos, 'secretarios': secretarios})


def pacientes_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'transplante/pacientes_detail.html', {'paciente': paciente})

def clinico_detail(request, pk):
    clinico = get_object_or_404(Clinico, pk=pk)
    return render(request, 'transplante/clinico_detail.html', {'clinicos': clinicos})

def secretario_detail(request, pk):
    secretario = get_object_or_404(Secretario, pk=pk)
    return render(request, 'transplante/secretario_detail.html', {'secretarios': secretarios})

def paciente_new(request):
	form = PacienteForm()
	return render(request, 'transplante/pacientes_edit.html', {'form': form})

def pacientes_edit(request,pk):
     paciente = get_object_or_404(Paciente, pk=pk)
     if request.method == "POST":
         form = PacienteForm(request.POST, instance=paciente)
         if form.is_valid():
             paciente.save()
             return redirect('pacientes_detail', pk=paciente.pk)
     else:
         form = PacienteForm(instance=paciente)
     return render(request, 'transplante/pacientes_edit.html', {'form': form})
        
