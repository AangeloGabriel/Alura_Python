lista = []

while True:
    nome = input("Digite o nome do ajudante: ")
    if nome == "Sair":
        print("Lista de pessoas: ", *lista, sep='\n')
        break
    else:
        lista.append(nome)

