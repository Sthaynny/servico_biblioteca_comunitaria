from django.db import models
from pyexpat import model


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255) 
    descricao =  models.CharField(max_length=1500)
    autor = models.CharField(max_length=255)
