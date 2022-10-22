from django.contrib.auth import authenticate, login
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound, JsonResponse)
from django.shortcuts import render

# Create your views here.
from .models import User


def criarUsuario(request):
    if request.method == 'POST':
        User.objects.create_user(request.POST['usuario'], request.POST['email'], request.POST['senha']);
        return HttpResponse()
    else:
        return HttpResponseNotFound()
    
    

def loginApp(request):
    username = request.POST['usuario']
    password = request.POST['senha']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({"token": request.session})
        else:
            return HttpResponseBadRequest({"mensagem": "conta desabilitada"})
    else:
        return HttpResponseBadRequest({"mensagem": "login invalido"})

def logout(request):
    logout(request)
    return HttpResponse()
