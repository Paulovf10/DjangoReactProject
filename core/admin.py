from django.contrib import admin

from core.models import Equipe, Meta, AtualizarMeta
from custom_auth.models import UserProfile
from django.contrib.auth.models import Group


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    search_fields = ('nome',)
    filter_horizontal = ('colaboradores',)


class MetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipoMeta', 'ativo')
    search_fields = ('nome',)
    filter_horizontal = ('colaboradores', 'equipe')


class AtualizarMetaAdmin(admin.ModelAdmin):
    list_display = ('meta', 'criadoEm')
    search_fields = ('meta',)


admin.site.unregister(Group)
admin.site.register(UserProfile)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(AtualizarMeta, AtualizarMetaAdmin)
