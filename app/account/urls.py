from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginApp, name='login',),
    path('logout', views.logoutApp, name='logout'),
    path('cadastrar', views.criarUsuario, name='cadastrar'),
    path('users', views.getUsuario, name='getUsuarios'),
]
