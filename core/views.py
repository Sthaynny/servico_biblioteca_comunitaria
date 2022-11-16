from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions, viewsets
from rest_framework.parsers import JSONParser

from .models import Emprestimo, List, Livro
from .serializers import EmprestimoSerializer, ListSerializer, LivroSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer 

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)

@csrf_exempt
def criar_emprestimo(request):
    if request.method == 'POST':
         
        name =   request.POST('user')
        id_livro =  request.POST('id_livro')
        print(name)
        print(id_livro)
       
        users = User.objects.all()
        livros = Livro.objects.all()  
        lists = List.objects.all()
        getList = None
        print(lists)
        for element in livros:
            if(element.id == id_livro):
                livro = element
        for element in users:
            if(element.username == name):
                user = element

        for list in lists:
            if(list.owner.username==name):
                getList = list 


        if getList is not None:
            getList = List(owner=user)
            getList.save();
        
        serializer = Emprestimo(list=getList.__str__, livro= livro)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)