from django.db import models


# Create your models here.
class TokenUsuario(models.Model):
    token = models.CharField(max_length=1500)
    user = models.CharField(max_length=250)
