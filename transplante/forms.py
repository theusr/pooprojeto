from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'telefone', 'cpf', 'email', 'data_nasc', 'tipo_sanguineo', 'orgao', 'alergia', 'doenca_preexist')
