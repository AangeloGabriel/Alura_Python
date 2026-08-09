from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 23.00, 'Medio')
prato_pao = Prato('Paozinho', 2.00, 'O melhor pao')
sobremesa_sorvete = Sobremesa('Sorvete', 'Casquinha', 'Pequena', 'Sorvete de Baunilha', 3.99)

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()