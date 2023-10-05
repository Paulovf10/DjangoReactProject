from django.db import models

from custom_auth.models import UserProfile


class Equipe(models.Model):
    """
        Classe referente ao modelo de Gestores.
    """
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
        related_name="equipes"
    )
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    ativo = models.BooleanField(blank=True, null=True, verbose_name='Ativo?')

    def __str__(self):
        return self.nome or u''

    class Meta:
        verbose_name = u'Equipe'
        verbose_name_plural = u'1. Equipes'

