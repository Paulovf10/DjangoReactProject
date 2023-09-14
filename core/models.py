from django.db import models
from . import settings


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Telefone', null=True, blank=True)
    subject = models.CharField(max_length=50, verbose_name='Assunto', null=True, blank=True)
    message = models.TextField(verbose_name='Mensagem', )
    is_read = models.BooleanField(verbose_name='Lido?', default=False)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)

    def str(self):
        return self.name or u''

    class Meta:
        verbose_name = u'Contato'
        verbose_name_plural = u'Contatos'
