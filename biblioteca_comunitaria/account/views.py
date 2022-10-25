from tokenize import String

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound, JsonResponse)
from django.shortcuts import render
from .models import TokenUsuario

def retornarBadRequest(_mensagem:String):
    return HttpResponseBadRequest(_mensagem)


def criarUsuario(request):
    if request.method == 'POST':
        try:
            user = User(username=request.POST['user'], email=request.POST['email'], password=request.POST['senha'])
            user.is_staff = True
            user.save();
            return HttpResponse(user.username)
        except:
            return retornarBadRequest("usuario ja existe")
    else:
        return HttpResponseNotFound()
    
    

def loginApp(request):
    if request.method == 'POST':
        try:
            user_name = request.POST['user']
            user_senha = request.POST['senha']
            print(user_name)
            print(user_senha)
            user = authenticate(request,username=user_name, password=user_senha)
            print(user)
            if user is not None:
                print (user.is_active)
                if user.is_active:
                    login(request, user)
                    return JsonResponse({"token": user.get_session_auth_hash()}, safe=False)
                else:
                    return retornarBadRequest("conta desabilitada")
            else:
                return retornarBadRequest("login invalido")        
        except:
            return retornarBadRequest("Erro ao executar o login")
    else:
        return HttpResponseNotFound()
    

def logoutApp(request):
    if request.method == 'POST':
        logout(request)
        request
        return HttpResponse()
    else:
        return HttpResponseNotFound()
    

def to_json(_user: User):
    return {"user": _user.username, "senha": _user.password,}


def getUsuario(request):
    usuarios = User.objects.all()
    data = []
    for usuario in usuarios:
        data.append(to_json(usuario))
    return JsonResponse(data, safe=False)
