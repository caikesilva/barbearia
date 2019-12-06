from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):

	sexos = (
		('M' , 'Masculino'),
		('F' , 'Feminino'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
	telefone = models.CharField(max_length=14)
	sexo = models.CharField(max_length=1, blank=False, choices=sexos)

	def __str__(self):
		return self.user.username

class Servico(models.Model):
	nome = models.CharField(max_length=200, blank=False)
	descricao = models.TextField()
	preco = models.FloatField()

	def __str__(self):
		return self.nome

class Agendamento(models.Model):
	data_solicitacao = models.DateTimeField(auto_now=True, null=False)
	data_agendamento = models.DateField(null=False)
	hora = models.TimeField(null=False)
	servico = models.ForeignKey('Servico', on_delete=models.CASCADE)
	cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
		return self.servico.nome+"  -  "+str(self.data_agendamento)

class Post(models.Model):
	data_publicacao = models.DateField(auto_now=True, null=False)
	titulo = models.CharField(max_length=200, blank=False)
	descricao = models.TextField(blank=False)
	imagem = models.ImageField(upload_to='blog/posts', blank=False)
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	def __str__(self):
		return self.titulo


class Galeria(models.Model):
	titulo = models.CharField(max_length=200, blank=False)
	imagem = models.ImageField(upload_to='galeria/posts', blank=False)

	def __str__(self):
		return self.titulo


