# O clube de atletismo Alura Runners organizou uma corrida e 
# divulgou a lista com a classificação final dos participantes. 
# Mas, um erro foi identificado: um dos nomes está incorreto. 
# O organizador precisa de um programa que permita localizar o 
# nome errado e substituí-lo pelo correto.

# Como você escreveria um programa que solicite o nome errado, 
# o nome correto e atualize a lista exibindo a nova classificação ao final?

# SOLUCAO

ListaAtletas = ['Lucas', 'Joao', 'Kaique']

nomeIncorreto = input("Digite o nome incorreto: ")

nomeCorreto = input("Agora digite o nome completo: ")

if nomeIncorreto in ListaAtletas:
    lugar = ListaAtletas.index(nomeIncorreto)
    ListaAtletas.remove(nomeIncorreto)
    ListaAtletas.insert(lugar, nomeCorreto)
    print(ListaAtletas)
else:
    print("Este nome nao consta na lista")
