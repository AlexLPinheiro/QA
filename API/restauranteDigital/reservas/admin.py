from django.contrib import admin
from .models import Mesa, Reserva

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Mesas no admin.
    """
    list_display = ('numero', 'capacidade')
    ordering = ('numero',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Reservas no admin.
    """
    list_display = ('cliente', 'mesa', 'data_hora', 'numero_pessoas')
    list_filter = ('data_hora', 'mesa')
    search_fields = ('cliente__username',)
    date_hierarchy = 'data_hora'