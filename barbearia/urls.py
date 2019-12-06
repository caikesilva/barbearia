from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('form_login', views.form_login, name='form_login'),
    path('posts', views.posts, name='posts'),
    path('contato', views.contato, name='contato'),
    path('servicos', views.servicos, name='servicos'),
    path('sobre', views.sobre, name='sobre'),
    path('form_cadastro_conta', views.form_cadastro_conta, name='form_cadastro_conta'),
    path('cadastrar_conta', views.cadastrar_conta, name='cadastrar_conta'),
    path('cadastrar_cliente', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('entrar', views.entrar, name='entrar'),
    path('sair', views.sair, name='sair'),
    path('form_agendamento', views.form_agendamento, name='form_agendamento'),
    path('agendamento', views.agendamento, name='agendamento'),
    path('meus_agendamentos/<int:pk>/', views.meus_agendamentos, name='meus_agendamentos'),
    path('meus_dados/<int:pk>/', views.meus_dados, name='meus_dados'),
    path('alterar_dados/<int:pk>/', views.alterar_dados, name='alterar_dados'),
    path('excluir_agendamento/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('form_alterar_agendamento/<int:pk>/', views.form_alterar_agendamento, name='form_alterar_agendamento'),
    path('alterar_agendamento/<int:pk>/', views.alterar_agendamento, name='alterar_agendamento'),
    path('email', views.email, name='email'),
    path('form_alterar_senha', views.form_alterar_senha, name='form_alterar_senha'),
    path('nova_senha', views.nova_senha, name='nova_senha'),
]
