from rest_framework import serializers

from .models import Emprestimo, Livro

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'autor', 'imagem']

class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    livro = LivroSerializer(many=True)
    class Meta:
        model = Emprestimo
        fields = ['name', 'owner', 'url', 'livro']
