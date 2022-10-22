from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='getLivros',),
    path('logout', views.logout, name='cadastrar'),
    path('cadastro', views.criarUsuario, name='atualizar'),
]
