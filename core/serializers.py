from app.serializers import UserSerializer
from rest_framework import serializers

from .models import Emprestimo, Livro


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['url', 'titulo', 'descricao', 'autor', 'imagem']

class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    livro = LivroSerializer() 
    class Meta:
        model = Emprestimo
        fields = [ 'url', 'owner', 'livro']
