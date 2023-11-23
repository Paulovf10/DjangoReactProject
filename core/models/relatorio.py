from django.db import models

from core.choices import TIPO_META, TIPO_NOTA
from core.models import Equipe
from custom_auth.models import UserProfile


class Relatorio(models.Model):
    tipoRelatorio = models.SmallIntegerField(choices=TIPO_META, verbose_name='Tipo de relatorio', null=True, blank=True)
    colaborador = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                    limit_choices_to={'type_user': 3},
                                    blank=True,
                                    null=True,
                                    verbose_name="Colaborador", )
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               verbose_name="Equipe", )

    quantidade = models.IntegerField(verbose_name='Quantidade de metas', blank=True, null=True)
    finalizadas = models.IntegerField(verbose_name='Mentas concluidas', blank=True, null=True)
    emAberto = models.IntegerField(verbose_name='Metas em aberto', blank=True, null=True)
    naoFinalizadas = models.IntegerField(verbose_name='Metas não finalizadas', blank=True, null=True)
    taxaSucesso = models.IntegerField(verbose_name='Taxa de sucesso', blank=True, null=True)
    notaFinal = models.SmallIntegerField(choices=TIPO_NOTA, verbose_name='Nota final', null=True, blank=True)
    def progresso_percentual(self):
        if self.finalizadas and self.emAberto:
            return (self.finalizadas / self.emAberto) * 100
        return 0
    class Meta:
        verbose_name = u'4. Relatorio'
        verbose_name_plural = u'4. Relatorios'
