from rest_framework import generics
from .models import Categoria
from .serializers import CategoriaSerializer

class ListaCardapioView(generics.ListAPIView):
    """
    Endpoint para listar todas as categorias e os itens dentro delas.
    """
    queryset = Categoria.objects.prefetch_related('itens').all()
    serializer_class = CategoriaSerializer