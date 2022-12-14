"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from core.views import EmprestimoViewSet, ListViewSet, LivroViewSet

from .views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'livro', LivroViewSet)
router.register(r'lists', ListViewSet, basename='list')
router.register(r'emprestimo', EmprestimoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token, name='api-tokn-auth'),  
    path('admin/', admin.site.urls),
]
