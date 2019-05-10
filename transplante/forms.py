from django import forms

from .models import Paciente, Clinicos

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc', 'tipo_sanguineo', 'orgao', 'alergia', 'doenca_preexist')




class ClinicosForm(forms.ModelForm):

    class Meta:
        model = Clinicos
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc', 'setor', 'profissao', 'CRM_CRE', 'especialidade')


