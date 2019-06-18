from django.contrib import admin
from .models import Pessoa, Paciente, Clinico, Secretario, Cirurgia

admin.site.register(Paciente)
admin.site.register(Clinico)
admin.site.register(Secretario)
admin.site.register(Cirurgia)
