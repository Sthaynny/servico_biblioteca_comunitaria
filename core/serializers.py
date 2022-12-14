from rest_framework import serializers

from .models import Emprestimo, List, Livro


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'url', 'titulo', 'descricao', 'autor', 'base64']

class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    livro = LivroSerializer() 
    
    class Meta:
        model = Emprestimo
        fields = [ 'id', 'url', 'livro' , 'aprovado', ]

class ListSerializer(serializers.HyperlinkedModelSerializer):
    emprestimo_set = EmprestimoSerializer(many=True) 
    
    class Meta:
        model = List
        fields = ['owner', 'url', 'emprestimo_set']
       
