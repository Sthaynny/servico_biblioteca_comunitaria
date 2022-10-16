from django.db import models
from pyexpat import model


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    img = models.CharField;
    descricao =  models.CharField(max_length=2000)
    ano = models.CharField(max_length=255)
