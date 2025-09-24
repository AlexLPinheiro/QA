from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Mesa {self.numero} ({self.capacidade} lugares)"

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    numero_pessoas = models.PositiveIntegerField()

    class Meta:
        unique_together = ('mesa', 'data_hora') # Evita duas reservas na mesma mesa e horário

    def __str__(self):
        return f"Reserva para {self.cliente.username} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"