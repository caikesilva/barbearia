from django.shortcuts import render
from . models import Post, Servico, Galeria, Cliente, Agendamento
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from random import choice
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
	fotos = Galeria.objects.all()
	servicos = Servico.objects.all()
	return render(request,'barbearia/index.html',{'servicos': servicos, 'fotos': fotos})

def form_login(request):
	return render(request, 'barbearia/form_login.html')

def posts(request):
	posts = Post.objects.all()
	posts_recentes = Post.objects.all().order_by('-data_publicacao')
	return render(request, 'barbearia/posts.html',{'posts': posts, 'posts_recentes':posts_recentes})
def contato(request):
	return render(request, 'barbearia/contato.html')

def servicos(request):
	servicos = Servico.objects.all()
	return render(request, 'barbearia/servicos.html', {'servicos': servicos})

def sobre(request):
	return render(request, 'barbearia/sobre.html')

def form_cadastro_conta(request):
	return render(request, 'barbearia/form_cadastro.html')

def cadastrar_conta(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	try:
		u = User.objects.get(username=username, email=email)

	except ObjectDoesNotExist:
		user = User.objects.create_user(username, email, password)
		user.save()
		return render(request, 'barbearia/form_cadastro_cliente.html',{'user': user})
	else:
		msg_erro = 'Usuario ou email já estão cadastrados!'
		return render(request, 'barbearia/form_cadastro.html',{'msg_erro': msg_erro})
		
def cadastrar_cliente(request):
	user_id = request.POST['user']
	sexo = request.POST['sexo']
	telefone = request.POST['telefone']
	user = User.objects.get(id=user_id)
	Cliente.objects.create(user=user, telefone=telefone,sexo=sexo)
	msg = 'cadastrado com suecesso'
	return render(request, 'barbearia/form_cadastro.html', {'msg': msg})

def entrar(request):
	servicos = Servico.objects.all()
	username = request.POST['username']
	password = request.POST['password']
	cliente = authenticate(username=username, password=password)
	if cliente is not None:
		login(request, cliente)
		return render(request, 'barbearia/form_agendamento.html',{'cliente': cliente, 'servicos': servicos})
	else:
		msg_erro = 'Usuario ou senha incorretos'
		return render(request, 'barbearia/form_login.html',{'msg_erro': msg_erro})

def sair(request):
	logout(request)
	return render(request, 'barbearia/form_login.html',{})

def agendamento(request):
	hora = request.POST['hora']
	data = request.POST['data']
	user = User.objects.get(id=request.POST['cliente'])
	servico = Servico.objects.get(id=request.POST['servico'])
	agendamento = Agendamento.objects.create(data_agendamento=data, hora=hora, servico=servico, cliente=user)
	msg = 'Agendamento Concluido'
	return render(request, 'barbearia/form_agendamento.html',{'msg': msg})

def meus_agendamentos(request, pk):
	meus_agendamentos = Agendamento.objects.filter(cliente_id=pk).order_by('-data_agendamento')
	return render(request, 'barbearia/meus_agendamentos.html',{'meus_agendamentos': meus_agendamentos})

def excluir_agendamento(request, pk):
	agendamento = Agendamento.objects.get(id=pk)
	agendamento.delete()
	msg = 'Excluido com Sucesso'
	return render(request, 'barbearia/index.html', {'msg': msg})

def form_alterar_agendamento(request, pk):
	agendamentos = Agendamento.objects.get(id=pk)
	return render(request, 'barbearia/form_alterar.html', {'agendamentos': agendamentos})

def form_agendamento(request):
	servicos = Servico.objects.all()
	return render(request, 'barbearia/form_agendamento.html', {'servicos': servicos})

def alterar_agendamento(request, pk):
	data = request.POST['data']
	hora = request.POST['hora']
	user = User.objects.get(id=request.POST['cliente'])
	servico = Servico.objects.get(id=request.POST['servico'])
	Agendamento.objects.filter(pk=pk).update(data_agendamento=data, hora= hora, servico=servico, cliente=user)
	msg = 'Alterado com Sucesso' 
	return render(request, 'barbearia/index.html', {'msg': msg})

def email(request):
	username = request.POST['name']
	subject = request.POST['subject']
	message = request.POST['message']
	email = request.POST['email']
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['.ks@gmail.com']
	
	if subject and message and email_from:
		send_mail(subject,message+'\nNome: '+username+'\nEmail: '+email, email_from,recipient_list)

	msg = 'Seu email foi enviado com sucesso.'
	return render(request, 'barbearia/contato.html',{'msg': msg})


def form_alterar_senha(request):
	return render(request, 'barbearia/form_alterar_senha.html')

def nova_senha(request):
	email = request.POST['email']	
	username = request.POST['user']
	sequencia = 'abcdefghijk1234567890'
	senha = ''
	#Gerando sequencia de 12 digitos aleatoria
	for x in range(12):
		senha += choice(sequencia)

	user = User.objects.get(username=username,email=email)
	user.set_password(senha)
	user.save()
	if user is not None:
		#enviando email com a nova senha
		subject = 'Nova Senha'
		message = 'Olá, '+str(username)+', sua nova senha é: '+str(senha)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]
		send_mail(subject,message,email_from,recipient_list)
		msg = 'Senha alterada com sucesso!'
		return render(request, 'barbearia/form_login.html',{'msg': msg})
	else:
		msg_erro = 'Email informado não está cadastrado!'
		return render(request, 'barbearia/form_login.html',{'msg_erro': msg_erro})

def meus_dados(request, pk):
	user = User.objects.get(pk=pk)
	cliente = Cliente.objects.get(user_id=pk)
	return render(request, 'barbearia/meus_dados.html',{'user': user, 'cliente': cliente})

def alterar_dados(request, pk):
	email = request.POST['email']
	password = request.POST['password']
	telefone = request.POST['telefone']
	sexo = request.POST['sex']
	user = User.objects.get(pk=pk)
	user.set_email(email)
	user.set_password(senha)
	user.save()
	cliente = Cliente.objects.get(user_id=pk).update(telefone=telefone)
	msg = 'Alterado com sucesso'
	return render(request, 'barbearia/meus_dados.html',{'msg': msg})
