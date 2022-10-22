import json
from email.mime import image
from http.client import HTTPResponse
from warnings import catch_warnings

from django.core import serializers
from django.http import (HttpResponseBadRequest, HttpResponseNotFound,
                         JsonResponse)
from django.shortcuts import render

from .models import Livro


def to_json(_livro: Livro):
    return {"titulo": _livro.titulo, "descricao": _livro.descricao, "autor": _livro.autor, "imagem": _livro.imagem.url, }


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
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        descricao = request.POST['descricao']
        imagem = request.FILES['imagem']
        livro = Livro(titulo=titulo, autor=autor,
                      descricao=descricao, imagem=imagem)
        livro.save()
        return JsonResponse(to_json(livro), safe=False)
    else:
        return HttpResponseNotFound()


def excluir(request, id):
    if request.method == 'DELETE':
        try:
            livro = Livro.objects.get(id=id)
            livro.delete()
            return JsonResponse(to_json(livro))
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()


def atualizar(request, id):
    if request.method == 'POST':
        try:
            livro = Livro.objects.get(id=id)
            livro.titulo = request.POST['titulo']
            livro.autor = request.POST['autor']
            livro.descricao = request.POST['descricao']
            livro.imagem = request.FILES['imagem']
            livro.save()
            return JsonResponse(to_json(livro))
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()
