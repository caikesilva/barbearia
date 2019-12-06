from django.contrib import admin
from django.contrib.auth.models import Group, User
from . models import Cliente, Servico, Agendamento, Post, Galeria
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Agendamento)
admin.site.register(Post)
admin.site.register(Galeria)

admin.site.unregister(Group)
admin.site.unregister(User)