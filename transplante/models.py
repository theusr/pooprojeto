from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Pessoa (models.Model):
		nome = models.CharField(max_length=200, default = '', verbose_name='Nome')
		telefone = models.CharField(max_length=15, default = '', verbose_name='Telefone')
		cpf = models.CharField(max_length=11, default = '', verbose_name='CPF')
		email = models.CharField(max_length=100, default = '', verbose_name='e-Mail')
		data_nasc = models.CharField(max_length=10, default = '', verbose_name='Data de Nascimento')

		def __str__(self):
		    return self.nome

class Paciente (Pessoa):
		doador_receptor = models.CharField(max_length=30, default = '', verbose_name='Doador ou Receptor')
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


class Secretario (Pessoa):
		registro_funcionario = models.CharField(max_length=50, default = '', verbose_name='Registro do Funcionário')

class Cirurgia(models.Model):
		data_hora = models.DateTimeField(max_length=30, default = '', verbose_name='Data e Hora da Cirurgia')
		sala_cirurgia = models.CharField(max_length=15, default = '', verbose_name='Sala da Cirurgia')
		sala_recuperacao = models.CharField(max_length=15, default = '', verbose_name='Sala de Recuperação')
		orgao = models.CharField(max_length=20, default = '', verbose_name='Órgão')
		tempo_duracao = models.CharField(max_length=30, default = '', verbose_name='Tempo de Duração da Cirurgia')
		equipamento = models.CharField(max_length=100, default = '', verbose_name='Equipamento Necessário')
		doador = models.ForeignKey('Paciente', on_delete=models.PROTECT, null=True, related_name = 'doador')
		receptor = models.ForeignKey('Paciente', on_delete=models.PROTECT, null=True, related_name = 'receptor')
		medico_responsavel = models.ForeignKey('Clinico', on_delete=models.PROTECT, null=True, related_name = 'medico')
		enfermeiro_responsavel = models.ForeignKey('Clinico', on_delete=models.PROTECT, null=True, related_name = 'enfermeiro')


class Sistema:
	pacientes = []
	clinicos = []
	secretarios = []
	cirurgias = []


	def RegistraPaciente(self, nome, telefone, cpf, email, data_nasc, doador_receptor, tipo_sanguineo, orgao, alergia, doenca_preexist):
		self.pacientes.append(Paciente(nome, telefone, cpf, email, data_nasc, doador_receptor, tipo_sanguineo, orgao, alergia, doenca_preexist))

	def RegistraClinico(self,nome, telefone, cpf, email, data_nasc, id_clinico, setor, profissao, CRM_CRE, especialidade):
		self.clinicos.append(Clinico(nome, telefone, cpf, email, data_nasc, id_clinico, setor, profissao, CRM_CRE, especialidade))

	def RegistraSecretario(self, nome, telefone, cpf, email, data_nasc, registro_funcionario):
		self.secretarios.append(Secretario(nome, telefone, cpf, email, data_nasc, registro_funcionario))

	def RegistraCirurgia(self, data_hora, sala_cirurgia, sala_recuperacao, orgao, tempo_duracao, equipamento, doador, receptor, medico_responsavel, enfermeiro_responsavel):
		self.cirurgias.append(Cirurgia(data_hora, sala_cirurgia, sala_recuperacao, orgao, tempo_duracao, equipamento, doador, receptor, medico_responsavel, enfermeiro_responsavel))





