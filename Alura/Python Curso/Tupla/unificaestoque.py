# estoque1 = ['Arroz', 'Feijão', 'Macarrão']
# estoque2 = ['Óleo', 'Sal', 'Açúcar']

# print(estoque1)
# print(estoque2)

# print(estoque1 + estoque2)

##################################################

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))

estoque_combinado = estoque1 + estoque2
print(estoque_combinado)