
from django.contrib.auth.models import User
from django.http import (HttpResponseBadRequest, HttpResponseNotFound,
                         JsonResponse)

from ..account.models import TokenUsuario
from .models import Emprestimo, Livro


def to_json(_livro: Livro):
    return {"titulo": _livro.titulo, "descricao": _livro.descricao, "autor": _livro.autor, "imagem": _livro.imagem.url, }


# Create your views here.
def getLivros(request):
    if request.method == 'GET':
        listaLivros = Livro.objects.all().values()
        data = []
        for livro in listaLivros:
            emprestimo = Emprestimo.objects.get(id=livro['id'])
            if emprestimo is None:
                data.append(livro)
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

def emprestimoLivro(request):
    if request.method == 'POST':
        try:
            idLivro = request.POST['id']
            username = request.POST['username']
            livro = Livro.objects.get(id=idLivro)
            emprestimo = Emprestimo(tokenUsuario=username, idLivro=idLivro)
            emprestimo.save()
            return JsonResponse(to_json(livro))
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()

def meusEmprestimos(request, username):
    if request.method == 'GET':
        try:
            data = []
            emprestimos = Emprestimo.objects.all()
            for emprestimo in emprestimos:
                livro = Livro.objects.get(id=emprestimo.idLivro)
                data.append(livro)
            return JsonResponse(data)
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()
