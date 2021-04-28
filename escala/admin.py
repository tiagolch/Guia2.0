from django.contrib import admin
from .models import Evento, Escala


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['datas', 'ultima_alteracao']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'evento', 'observacao']


