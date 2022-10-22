

from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from .models import User


def criarUsuario(request):
    user = User.objects.create_user(request.POST['usuario'], request.POST['email'], request.POST['senha']);
    

def my_view(request):
    username = request.POST['usuario']
    password = request.POST['senha']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirecione para uma página de sucesso.
        else:
            # Retorna uma mensagem de erro de 'conta desabilitada' .
    else:
        # Retorna uma mensagem de erro 'login inválido'.
