from django import forms
from django.contrib.auth.models import User
from .models import Paciente, Clinico, Secretario

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'telefone', 'cpf', 'email','data_nasc', 'tipo_sanguineo', 'orgao', 'alergia', 'doenca_preexist')

class ClinicoForm(forms.ModelForm):

    class Meta:
        model = Clinico
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc', 'setor', 'profissao', 'CRM_CRE', 'especialidade')

class SecretarioForm(forms.ModelForm):

    class Meta:
        model = Secretario
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

