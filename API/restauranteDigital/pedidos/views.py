from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pedido
from .serializers import PedidoSerializer
from .mixins import ResponseTimeMixin # Importando o mixin

class CriarPedidoView(ResponseTimeMixin, generics.CreateAPIView): # Usando o Mixin
    """
    Endpoint para criar um novo pedido.
    Este endpoint mede e exibe o tempo de resposta no terminal.
    """
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        # Lógica para calcular o total do pedido seria adicionada aqui
        # Por simplicidade, o total será passado diretamente no POST
        serializer.save(cliente=self.request.user)