from django.contrib import admin
from .models import Pessoa, Paciente, Clinicos, Secretarios

admin.site.register(Secretarios)
admin.site.register(Pessoa)
admin.site.register(Paciente)
admin.site.register(Clinicos)
