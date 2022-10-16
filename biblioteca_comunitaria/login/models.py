from django.db import models


# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
