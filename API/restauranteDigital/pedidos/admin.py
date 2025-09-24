from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    # Em pedidos existentes, não queremos campos vazios por padrão
    extra = 0
    # Campos que não devem ser editados após o pedido ser feito
    readonly_fields = ('item_cardapio', 'quantidade', 'preco_unitario')

    # Impede que o admin possa adicionar ou deletar itens de um pedido já criado
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Pedidos no admin.
    """
    list_display = ('id', 'cliente', 'status', 'total', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('cliente__username', 'id')
    # Campos que são definidos automaticamente e não devem ser editados
    readonly_fields = ('cliente', 'criado_em', 'total')
    inlines = [ItemPedidoInline]
    date_hierarchy = 'criado_em'