from django.template import loader
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getLivros, name='getLivros',),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('emprestimo', views.emprestimoLivro, name='emprestimoLivro'),
    path('meus-emprestimos/<str:username>', views.meusEmprestimos, name='meusEmprestimos'),
    path('excluir-emprestimo/<int:id>', views.excluirEmprestimo, name='excluirEmprestimo'),
]
