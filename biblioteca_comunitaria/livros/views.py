from http.client import HTTPResponse
from telnetlib import STATUS

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
    if request.method == 'POST':
        titulo = request.POST['titulo'];
        autor = request.POST['autor'];
        descricao = request.POST['descricao'];
        livro = Livro(titulo=titulo, autor=autor, descricao=descricao)
        livro.save()
        return JsonResponse({"livro": titulo})
    else:
        return JsonResponse({"erro": "Algo inesperado aconteceu"}, status=404)

    
    

def excluir(id):
    return HTTPResponse('test')

def atualizar(id):
    return HTTPResponse('test')
