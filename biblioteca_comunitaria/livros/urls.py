from django.urls import path

from . import views
from django.template import loader
urlpatterns = [
    path('', views.getLivros, name='getLivros',),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('atualizar/', views.atualizar, name='atualizar'),
    path('excluir/', views.excluir, name='excluir'),
]
