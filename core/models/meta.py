from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.choices import TIPO_META, UNIDADE_MEDIDA_CHOICES
from core.models import Equipe
from core.models.atualizar_meta import AtualizarMeta
from custom_auth.models import UserProfile


class Meta(models.Model):
    """
    Classe referente ao modelo de Metas da empresa.
    """
    nome = models.CharField(max_length=50, verbose_name='Nome', null=True, blank=True)
    gestor = models.ForeignKey(
        UserProfile,
        limit_choices_to={'type_user': 2},
        related_name="gestor_metas",
        on_delete=models.CASCADE, null=True, blank=True
    )
    descricao = models.TextField(verbose_name='Descrição', null=True, blank=True)
    tipoMeta = models.SmallIntegerField(choices=TIPO_META, verbose_name='Tipo de meta', null=True, blank=True)
    valorAlvo = models.CharField(max_length=30, verbose_name='Valor Alvo', null=True, blank=True)
    progressoAtual = models.CharField(max_length=30, verbose_name='Progresso Atual', null=True, blank=True)
    unidadeMedida = models.SmallIntegerField(
        verbose_name='Unidade de Medida',
        choices=UNIDADE_MEDIDA_CHOICES,
        null=True,
        blank=True
    )
    dataInicio = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    dataFim = models.DateField(verbose_name='Data de Fim', null=True, blank=True)
    colaboradores = models.ManyToManyField(
        UserProfile,
        limit_choices_to={'type_user': 3},
        related_name="colaboradores_meta", null=True, blank=True
    )
    equipe = models.ManyToManyField(
        Equipe,
        related_name="equipes_meta", null=True, blank=True
    )
    metaBatida = models.BooleanField(default=False, verbose_name='Meta Batida')
    ativo = models.BooleanField(default=True, verbose_name='Ativo?')

    def __str__(self):
        return self.nome or u''

    def progresso_percentual(self):
        if self.valorAlvo and self.progressoAtual:
            return (self.progressoAtual / self.valorAlvo) * 100
        return 0

    def update_progress(self, valor):
        self.progressoAtual = float(self.progressoAtual) + float(valor)
        if self.progressoAtual >= float(self.valorAlvo):
            self.metaBatida = True
        self.save(update_fields=['progressoAtual', 'metaBatida'])

    class Meta:
        verbose_name = u'2. Meta'
        verbose_name_plural = u'2. Metas'

