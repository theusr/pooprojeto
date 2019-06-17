from django.db import models

# Create your models here.

class Pessoa (models.Model):
		nome = models.CharField(max_length=200, default = '', verbose_name='Nome')
		telefone = models.CharField(max_length=15, default = '', verbose_name='Telefone')
		cpf = models.CharField(max_length=11, default = '', verbose_name='CPF')
		email = models.CharField(max_length=100, default = '', verbose_name='e-Mail')
		data_nasc = models.CharField(max_length=10, default = '', verbose_name='Data de Nascimento')

class Paciente (Pessoa):
		tipo_sanguineo = models.CharField(max_length=3, default = '', verbose_name='Tipo Sanguíneo')
		orgao = models.CharField(max_length=20, default = '', verbose_name='Órgão')
		alergia = models.CharField(max_length=100, default = '', verbose_name='Alergias')
		doenca_preexist = models.CharField(max_length=100, default = '', verbose_name='Doença Pré-existente')


class Clinico (Pessoa):
		id_clinico = models.AutoField(primary_key=True)
		setor = models.CharField(max_length=100, default = '', verbose_name='Setor')
		profissao = models.CharField(max_length=50, default = '', verbose_name='Profissão')
		CRM_CRE = models.CharField(max_length=50, default = '', verbose_name='CRM ou CRE')
		especialidade = models.CharField(max_length=100, default = '', verbose_name='Especialidade')


class Secretario(Pessoa):
	pacientes = []
	clinicos = []
	secretarios = []


	def RegistraPaciente(self, nome, telefone, cpf, email, data_nasc, tipo_sanguineo, orgao, alergia, doenca_preexist):
		self.pacientes.append(Paciente(nome, telefone, cpf, email, data_nasc, tipo_sanguineo, orgao, alergia, doenca_preexist))

	def RegistraClinico(self, nome, telefone, cpf, email, data_nasc, id_clinico, setor, profissao, CRM_CRE, especialidade):
		self.clinicos.append(Clinico(nome, telefone, cpf, email, data_nasc, id_clinico, setor, profissao, CRM_CRE, especialidade))

	def RegistraSecretario(self, nome, telefone, cpf, email, data_nasc):
		self.secretarios.append(Secretario(nome, telefone, cpf, email, data_nasc))



