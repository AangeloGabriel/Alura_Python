from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de laranja', 23.00, 'Medio')
prato_pao = Prato('Paozinho', 2.00, 'O melhor pao')

restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_pao)

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()