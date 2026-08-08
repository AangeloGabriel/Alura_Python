# Paulo está criando uma lista de pedidos para a lanchonete. 
# Ele já tem todos os pedidos, mas percebeu que o último foi 
# inserido por engano e precisa removê-lo.

# Diante deste problema, ajude Paulo criando um programa que 
# automatize essa operação, permitindo listar os pedidos e s
# remover o último item automaticamente.

# Exemplo de Entrada:

# Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa

# Saída esperada: Pedidos finais: ['Sanduíche', 'Suco']


while True:
    pedido = input("Digite seu pedido: ").strip().split(',')
    confirmacao = input("Deseja deletar o ultimo item do pedido? ")
    if confirmacao == 'sim':
        pedido.pop()
        print(pedido)
        break
    else:
        print(pedido)
        break
