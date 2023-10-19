from django.db import models

from core.choices import TIPO_META
from core.models import Equipe
from custom_auth.models import UserProfile


class Meta(models.Model):
    """
        Classe referente ao modelo de Gestores.
    """
    nome = models.CharField(max_length=50, blank=False, null=True, verbose_name='Nome')
    descricao = models.TextField(blank=False, null=False, verbose_name='Descrição')
    tipo_meta = models.SmallIntegerField(verbose_name='Tipo de meta', null=True, blank=True, choices=TIPO_META)
    gestor = models.ForeignKey(
        UserProfile,
        limit_choices_to={'type_user': 2},
        blank=True, null=True,
        verbose_name="Gestor",
        on_delete=models.CASCADE
    )
    colaboradores = models.ManyToManyField(
        UserProfile,
        limit_choices_to={'type_user': 3},
        blank=True,
        null=True,
        verbose_name="Colaboradores",
        related_name="colaboradores_meta"
    )
    equipe = models.ManyToManyField(
        Equipe,
        blank=True,
        null=True,
        verbose_name="Equipe",
        related_name="equipes_meta"
    )
    ativo = models.BooleanField(blank=True, null=True, verbose_name='Ativo?')

    def __str__(self):
        return self.nome or u''

    class Meta:
        verbose_name = u'Meta'
        verbose_name_plural = u'2. Metas'
