from django.contrib import admin
from .models import Categoria, ItemCardapio

# Usando um 'inline' para gerenciar itens dentro da própria categoria
class ItemCardapioInline(admin.TabularInline):
    model = ItemCardapio
    # 'extra' define quantos campos vazios para novos itens serão exibidos
    extra = 1
    fields = ('nome', 'descricao', 'preco')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Categorias no admin.
    """
    list_display = ('nome',)
    search_fields = ('nome',)
    # Adiciona a gestão de Itens de Cardápio na página da Categoria
    inlines = [ItemCardapioInline]

@admin.register(ItemCardapio)
class ItemCardapioAdmin(admin.ModelAdmin):
    """
    Personaliza a exibição de Itens de Cardápio.
    Útil para ver todos os itens de uma vez, independente da categoria.
    """
    list_display = ('nome', 'categoria', 'preco')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
    list_per_page = 20