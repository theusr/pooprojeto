from django.db import models

# Create your models here.

class Pessoa (models.Model):
		nome = models.CharField(max_length=200, default = '')
		telefone = models.CharField(max_length=15, default = '')
		cpf = models.CharField(max_length=11, default = '')
		email = models.CharField(max_length=100, default = '')
		data_nasc = models.CharField(max_length=10, default = '')

class Paciente (Pessoa):
		tipo_sanguineo = models.CharField(max_length=3, default = '')
		orgao = models.CharField(max_length=20, default = '')
		alergia = models.CharField(max_length=100, default = '')
		doenca_preexist = models.CharField(max_length=100, default = '')


class Clinicos (Pessoa):
		id_clinicos = models.AutoField(primary_key=True)
		setor = models.CharField(max_length=100, default = '')
		profissao = models.CharField(max_length=50, default = '')
		CRM_CRE = models.CharField(max_length=50, default = '')
		especialidade = models.CharField(max_length=100, default = '')
     

class Secretarios (Pessoa):
	def __init__(self):
		id_secretario = models.AutoField(primary_key=True)
		self.pacientes = []
		self.clinicos = []

	def RegistraPaciente(self, nome, telefone, cpf, email, data_nasc, tipo_sanguineo, orgao, alergia, doenca_preexist):
		self.pacientes.append(Paciente(nome, telefone, cpf, email, data_nasc, tipo_sanguineo, orgao, alergia, doenca_preexist))

	def RegistraClinicos(self, nome, telefone, cpf, email, data_nasc, setor, profissao, CRM_CRE, especialidade):
		self.clinicos.append(Clinicos(nome, telefone, cpf, email, data_nasc, setor, profissao, CRM_CRE, especialidade))


