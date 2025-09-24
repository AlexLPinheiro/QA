from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='itens', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome