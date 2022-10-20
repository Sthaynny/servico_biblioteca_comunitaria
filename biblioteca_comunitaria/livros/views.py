import json
from http.client import HTTPResponse

from django.core import serializers
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from .models import Livro


def to_json(_livro: Livro):
        return {"titulo": _livro.titulo, "descricao": _livro.descricao, "autor":_livro.autor,}


# Create your views here.
def getLivros(request):
    if request.method == 'GET':
        listaLivros = Livro.objects.all().values() 
        data = []
        for element in listaLivros:
            data.append(element)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseNotFound()


def cadastrar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo'];
        autor = request.POST['autor'];
        descricao = request.POST['descricao'];
        livro = Livro(titulo=titulo, autor=autor, descricao=descricao)
        livro.save()
        return JsonResponse(to_json(livro), safe=False)
    else:
        return HttpResponseNotFound()

def excluir(request, id):
    return HTTPResponse('test')

def atualizar(id):
    return HTTPResponse('test')
