from django import forms
from django.contrib.auth.models import User
from .models import Paciente, Clinico, Secretario, Cirurgia

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome', 'telefone', 'cpf', 'email','data_nasc', 'doador_receptor', 'tipo_sanguineo', 'orgao', 'alergia', 'doenca_preexist')

class ClinicoForm(forms.ModelForm):
    class Meta:
        model = Clinico
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc', 'setor', 'profissao', 'CRM_CRE', 'especialidade')

class SecretarioForm(forms.ModelForm):
    class Meta:
        model = Secretario
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc')

class CirurgiaForm(forms.ModelForm):
    class Meta:
        model = Cirurgia
        fields = ('data_hora', 'sala_cirurgia', 'sala_recuperacao', 'orgao', 'tempo_duracao', 'equipamento', 'doador', 'receptor', 'medico_responsavel', 'enfermeiro_responsavel')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

