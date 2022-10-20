from django.template import loader
from django.urls import path

from . import views

urlpatterns = [
    path('', views.getLivros, name='getLivros',),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]
