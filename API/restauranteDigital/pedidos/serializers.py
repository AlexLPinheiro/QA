from rest_framework import serializers
from .models import Pedido, ItemPedido
from cardapio.serializers import ItemCardapioSerializer

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['item_cardapio', 'quantidade']

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'status', 'criado_em', 'total', 'itens']
        read_only_fields = ['cliente', 'status']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = Pedido.objects.create(**validated_data)
        total_pedido = 0

        for item_data in itens_data:
            item_cardapio = item_data['item_cardapio']
            quantidade = item_data['quantidade']
            preco = item_cardapio.preco
            total_pedido += (preco * quantidade)
            ItemPedido.objects.create(
                pedido=pedido,
                item_cardapio=item_cardapio,
                quantidade=quantidade,
                preco_unitario=preco
            )

        pedido.total = total_pedido
        pedido.save()
        return pedido