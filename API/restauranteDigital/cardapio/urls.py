from django.urls import path
from .views import ListaCardapioView

urlpatterns = [
    path('', ListaCardapioView.as_view(), name='lista-cardapio'),
]