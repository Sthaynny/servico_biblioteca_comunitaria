from django.contrib import admin

from .models import Emprestimo, Livro, List

admin.site.register(List)
admin.site.register(Livro)
admin.site.register(Emprestimo)
