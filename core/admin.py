from django.contrib import admin

from core.models import Equipe, Meta
from custom_auth.models import UserProfile
from django.contrib.auth.models import Group


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    search_fields = ('nome',)
    filter_horizontal = ('colaboradores',)


class MetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_meta', 'ativo')
    search_fields = ('nome',)
    filter_horizontal = ('colaboradores', 'equipe')

admin.site.unregister(Group)
admin.site.register(UserProfile)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Meta, MetaAdmin)
