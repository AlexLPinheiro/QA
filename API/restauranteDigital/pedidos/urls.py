from django.urls import path
from .views import CriarPedidoView

urlpatterns = [
    path('criar/', CriarPedidoView.as_view(), name='criar-pedido'),
]