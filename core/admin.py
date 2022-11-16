from django.contrib import admin

from .models import Emprestimo, List, Livro

admin.site.register(List)
admin.site.register(Livro)
admin.site.register(Emprestimo)