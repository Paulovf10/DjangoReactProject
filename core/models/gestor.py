from django.db import models


class Gestor(models.Model):
    """
        Classe referente ao modelo de Gestores.
    """
    nome = models.CharField(max_length=50, blank=False, null=True, verbose_name='Nome')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    senha = models.CharField(max_length=18, blank=False, null=False, verbose_name='Senha')
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    empresa = models.CharField(max_length=50, blank=True, null=True, verbose_name='Empresa')
    cargo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cargo')
    equipe = models.CharField(max_length=50, blank=True, null=True, verbose_name='Equipe')
    foto = models.FileField(blank=True, null=True, verbose_name='Foto de perfil', upload_to='perfil')

    def __str__(self):
        return self.nome or u''

    class Meta:
        verbose_name = u'Gestor'
        verbose_name_plural = u'1. Gestores'
