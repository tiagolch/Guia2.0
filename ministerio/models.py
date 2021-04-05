from django.db import models


class Ministerio(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Ministério')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Ministerios'


class Funcao(models.Model):
    ministerio_nome = models.ForeignKey('Ministerio', on_delete=models.DO_NOTHING, related_name='Ministério')
    funcao = models.CharField(max_length=50, verbose_name='Função')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.funcao}'

    class Meta:
        verbose_name_plural = 'Funcoes'




