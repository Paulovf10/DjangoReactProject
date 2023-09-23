from django.contrib import admin

from core.models import Gestor


class GestorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'dtNascimento', 'empresa', 'cargo', 'equipe')
    search_fields = ('nome', 'email', 'empresa')


admin.site.register(Gestor, GestorAdmin)
