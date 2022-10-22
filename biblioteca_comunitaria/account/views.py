from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound, JsonResponse)
from django.shortcuts import render


def criarUsuario(request):
    if request.method == 'POST':
        try:
            user = User(username=request.POST['user'], email=request.POST['email'], password=request.POST['senha'])
            user.save();
            return HttpResponse(user.username)
        except:
            return HttpResponseBadRequest("usuario ja existe")
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
