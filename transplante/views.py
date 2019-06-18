from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Clinico, Secretario, Sistema
from .forms import PacienteForm, ClinicoForm, SecretarioForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def home(request):
	return render (request, 'transplante/home.html', {'home': home})

def lista_pacientes(request):
	pacientes = Paciente.objects.order_by('nome').all()
	return render(request, 'transplante/lista_pacientes.html', {'pacientes': pacientes})

def lista_clinicos(request):
        clinicos = Clinico.objects.order_by('nome').all()
        return render(request, 'transplante/lista_clinicos.html', {'clinicos': clinicos})

def lista_secretarios(request):
        secretarios = Secretario.objects.order_by('nome').all()
        return render(request, 'transplante/lista_secretarios.html', {'secretarios': secretarios})

def pacientes_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'transplante/pacientes_detail.html', {'paciente': paciente})

def clinicos_detail(request, pk):
    clinico = get_object_or_404(Clinico, pk=pk)
    return render(request, 'transplante/clinicos_detail.html', {'clinico': clinico})

def secretarios_detail(request, pk):
    secretario = get_object_or_404(Secretario, pk=pk)
    return render(request, 'transplante/secretarios_detail.html', {'secretario': secretario})

def paciente_new(request):
     if request.method == "POST":
         form = PacienteForm(request.POST)
         if form.is_valid():
             paciente = form.save(commit=False)
             paciente.author = request.user
             paciente.save()
             return redirect('pacientes_detail', pk=paciente.pk)
     else:
         form = PacienteForm()
     return render(request, 'transplante/pacientes_edit.html', {'form': form})

def clinico_new(request):
     if request.method == "POST":
         form = ClinicoForm(request.POST)
         if form.is_valid():
             clinico = form.save(commit=False)
             clinico.author = request.user
             clinico.save()
             return redirect('clinicos_detail', pk=clinico.pk)
     else:
         form = ClinicoForm()
     return render(request, 'transplante/clinicos_edit.html', {'form': form})

def secretario_new(request):
     if request.method == "POST":
         form = SecretarioForm(request.POST)
         if form.is_valid():
             secretario = form.save(commit=False)
             secretario.author = request.user
             secretario.save()
             return redirect('secretarios_detail', pk=secretario.pk)
     else:
         form = SecretarioForm()
     return render(request, 'transplante/secretarios_edit.html', {'form': form})

def pacientes_edit(request,pk):
     paciente = get_object_or_404(Paciente, pk=pk)
     if request.method == "POST":
         form = PacienteForm(request.POST, instance=paciente)
         if form.is_valid():
             paciente = form.save(commit=False)
             paciente.author = request.user
             paciente.save()
             return redirect('pacientes_detail', pk=paciente.pk)
     else:
         form = PacienteForm(instance=paciente)
     return render(request, 'transplante/pacientes_edit.html', {'form': form})

def clinicos_edit(request,pk):
     clinico = get_object_or_404(Clinico, pk=pk)
     if request.method == "POST":
         form = ClinicoForm(request.POST, instance=clinico)
         if form.is_valid():
             clinico = form.save(commit=False)
             clinico.author = request.user
             clinico.save()
             return redirect('clinicos_detail', pk=clinico.pk)
     else:
         form = ClinicoForm(instance=clinico)
     return render(request, 'transplante/clinicos_edit.html', {'form': form})

def secretarios_edit(request,pk):
     secretario = get_object_or_404(Secretario, pk=pk)
     if request.method == "POST":
         form = SecretarioForm(request.POST, instance=secretario)
         if form.is_valid():
             secretario = form.save(commit=False)
             secretario.author = request.user
             secretario.save()
             return redirect('secretarios_detail', pk=secretario.pk)
     else:
         form = SecretarioForm(instance=secretario)
     return render(request, 'transplante/secretarios_edit.html', {'form': form})
        

def remove_paciente(request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return redirect('lista_pacientes')

def remove_clinico(request, pk):
        clinico = get_object_or_404(Clinico, pk=pk)
        clinico.delete()
        return redirect('lista_clinicos')

def remove_secretario(request, pk):
        secretario = get_object_or_404(Secretario, pk=pk)
        secretario.delete()
        return redirect('lista_secretarios')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Conta desativada')
            else:
                return HttpResponse('Login inválido')
    else:
        form = LoginForm()
    return render(request, 'transplante/login.html', {'form': form})
