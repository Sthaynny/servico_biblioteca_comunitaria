from rest_framework import authentication, permissions, viewsets

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
