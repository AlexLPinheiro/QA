from rest_framework import serializers
from .models import Categoria, ItemCardapio

class ItemCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCardapio
        fields = ['id', 'nome', 'descricao', 'preco']

class CategoriaSerializer(serializers.ModelSerializer):
    itens = ItemCardapioSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'itens']