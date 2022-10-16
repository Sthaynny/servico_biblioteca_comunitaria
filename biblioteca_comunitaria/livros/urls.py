from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='getLivros'),
    path('cadastrar/', views.index, name='cadastrar'),
    path('atualizar/', views.index, name='atualizar'),
    path('excluir/', views.index, name='excluir'),
]
