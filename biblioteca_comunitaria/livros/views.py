from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import render
from django.template import loader

from .models import Livro


# Create your views here.
def getLivros(request):
    listaLivros = Livro.objects.all().values() 
    if listaLivros.count() <= 0:
        data =  {
            'livros':[]
        }
    else: 
        data =  {
            'livros': listaLivros
        }

    return JsonResponse(data)

def cadastrar(request):
    
    template = loader.get_template('index.html')
    return HTTPResponse(template.render())

def excluir(id):
    return HTTPResponse('test')

def atualizar(id):
    return HTTPResponse('test')
