from django.contrib import admin

from .models import Emprestimo, Livro

# Register your models here.
admin.site.register(Livro)
admin.site.register(Emprestimo)
