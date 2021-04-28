from django.db import models

from account.models import User


class Evento(models.Model):
    data = models.DateTimeField()
    ultima_alteração = models.DateTimeField(auto_now=True)
    observacao = models.TextField(max_length=250, blank=True, null=True,)

    def __str__(self):
        return f'{self.data}'

    def datas(self):
        return self.data.strftime('%A - %d/%m/%Y %H:%M')

    def ultima_alteracao(self):
        return self.ultima_alteração.strftime('%d/%m/%Y %H:%M')


class Escala(models.Model):
    nome = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Responsavel')
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING, verbose_name='Evento')
    observacao = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

