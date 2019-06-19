from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Clinico, Secretario, Sistema, Cirurgia
from .forms import PacienteForm, ClinicoForm, SecretarioForm, CirurgiaForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

def lista_cirurgias(request):
        cirurgias = Cirurgia.objects.order_by('data_hora').all()
        return render(request, 'transplante/lista_cirurgias.html', {'cirurgias': cirurgias})

def pacientes_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'transplante/pacientes_detail.html', {'paciente': paciente})

def clinicos_detail(request, pk):
    clinico = get_object_or_404(Clinico, pk=pk)
    return render(request, 'transplante/clinicos_detail.html', {'clinico': clinico})

def secretarios_detail(request, pk):
    secretario = get_object_or_404(Secretario, pk=pk)
    return render(request, 'transplante/secretarios_detail.html', {'secretario': secretario})

def cirurgias_detail(request, pk):
    cirurgia = get_object_or_404(Cirurgia, pk=pk)
    return render(request, 'transplante/cirurgias_detail.html', {'cirurgia': cirurgia})

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

def cirurgia_new(request):
     if request.method == "POST":
         form = CirurgiaForm(request.POST)
         if form.is_valid():
             cirurgia = form.save(commit=False)
             cirurgia.author = request.user
             cirurgia.save()
             return redirect('cirurgias_detail', pk=cirurgia.pk)
     else:
         form = CirurgiaForm()
     return render(request, 'transplante/cirurgias_edit.html', {'form': form})


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

def cirurgias_edit(request,pk):
     cirurgia = get_object_or_404(Cirurgia, pk=pk)
     if request.method == "POST":
         form = CirurgiaForm(request.POST, instance=cirurgia)
         if form.is_valid():
             cirurgia = form.save(commit=False)
             cirurgia.author = request.user
             cirurgia.save()
             return redirect('cirurgias_detail', pk=cirurgia.pk)
     else:
         form = CirurgiaForm(instance=cirurgia)
     return render(request, 'transplante/cirurgias_edit.html', {'form': form})
        

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

def remove_cirurgia(request, pk):
        cirurgia = get_object_or_404(Cirurgia, pk=pk)
        cirurgia.delete()
        return redirect('lista_cirurgias')

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

def formView(request):
        if request.session.has_key('username'):
                username = request.session['username']
                return render(request, 'home.html', {'username' : username})
        else:
                return render(request, 'transplante/login.html', {})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('logout.html')


def busca_pacientes(request):
	if request.method == 'GET':
		search_query = request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if search_query is not None:
			lookups=Q(nome__icontains=search_query) | Q(orgao__icontains=search_query) | Q(cpf__icontains=search_query)
			results=Paciente.objects.filter(lookups).distinct()
			context={'results': results, 'submitbutton': submitbutton}
			return render(request, 'transplante/busca_pacientes.html', context)


		else:
			return render(request, 'transplante/busca_pacientes.html')

	else:
		return render(request, 'transplante/busca_pacientes.html')

def busca_clinicos(request):
	if request.method == 'GET':
		search_query = request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if search_query is not None:
			lookups=Q(nome__icontains=search_query) | Q(profissao__icontains=search_query) | Q(setor__icontains=search_query)
			results=Clinico.objects.filter(lookups).distinct()
			context={'results': results, 'submitbutton': submitbutton}
			return render(request, 'transplante/busca_clinicos.html', context)


		else:
			return render(request, 'transplante/busca_clinicos.html')

	else:
		return render(request, 'transplante/busca_clinicos.html')

def busca_secretarios(request):
	if request.method == 'GET':
		search_query = request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if search_query is not None:
			lookups=Q(nome__icontains=search_query) | Q(registro_funcionario__icontains=search_query) | Q(cpf__icontains=search_query)
			results=Secretario.objects.filter(lookups).distinct()
			context={'results': results, 'submitbutton': submitbutton}
			return render(request, 'transplante/busca_secretarios.html', context)


		else:
			return render(request, 'transplante/busca_secretarios.html')

	else:
		return render(request, 'transplante/busca_secretarios.html')

def busca_cirurgias(request):
	if request.method == 'GET':
		search_query = request.GET.get('q')
		submitbutton= request.GET.get('submit')

		if search_query is not None:
			lookups=Q(data_hora__icontains=search_query) | Q(sala_cirurgia__icontains=search_query) | Q(orgao__icontains=search_query)
			results=Cirurgia.objects.filter(lookups).distinct()
			context={'results': results, 'submitbutton': submitbutton}
			return render(request, 'transplante/busca_cirurgias.html', context)


		else:
			return render(request, 'transplante/busca_cirurgias.html')

	else:
		return render(request, 'transplante/busca_cirurgias.html')


class MyView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


