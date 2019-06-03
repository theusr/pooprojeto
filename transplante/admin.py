from django.contrib import admin
from .models import Pessoa, Paciente, Clinico, Secretario

admin.site.register(Paciente)
admin.site.register(Clinico)
admin.site.register(Secretario)
