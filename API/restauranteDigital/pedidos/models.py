from django.db import models
from django.contrib.auth.models import User
from cardapio.models import ItemCardapio # Acoplamento controlado

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('recebido', 'Recebido'),
        ('preparando', 'Em Preparação'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='recebido')
    criado_em = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.item_cardapio.nome}"