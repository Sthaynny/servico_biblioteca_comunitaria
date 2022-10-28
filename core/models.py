from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255) 
    descricao =  models.CharField(max_length=1500)
    autor = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="imgs",default=None)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro= models.ForeignKey(Livro,on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.livro.titulo
