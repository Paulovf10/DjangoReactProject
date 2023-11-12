from django.db import models


class AtualizarMeta(models.Model):
    meta = models.ForeignKey('Meta', on_delete=models.CASCADE, related_name='atualizacoes')
    comentario = models.TextField(verbose_name='Comentário', blank=True)
    valorAtualizacao = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor de Atualização')
    criadoEm = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criado em')
    def __str__(self):
        return f"Atualização para {self.meta.nome} - {self.valorAtualizacao}"

    class Meta:
        verbose_name = u'3. Atualizar Meta'
        verbose_name_plural = u'3. Atualizar Metas'
