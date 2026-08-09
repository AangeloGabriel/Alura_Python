from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, tipo, tamanho, descricao, preco):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.descricao = descricao
        self.tamanho = tamanho

    def __str__(self):
        self._nome

    def aplicar_desconto(self):
        ...