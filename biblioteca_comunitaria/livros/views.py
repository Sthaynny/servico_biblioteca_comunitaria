from http.client import HTTPResponse

from django.shortcuts import render


# Create your views here.
def getLivros():
    return HTTPResponse('test')

def cadastrar():
    return HTTPResponse('test')

def excluir():
    return HTTPResponse('test')

def atualizar():
    return HTTPResponse('test')
