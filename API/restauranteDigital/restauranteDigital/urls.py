from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cardapio/', include('cardapio.urls')),
    path('api/pedidos/', include('pedidos.urls')),
    # path('api/reservas/', include('reservas.urls')), # Adicionaríamos quando implementado
]