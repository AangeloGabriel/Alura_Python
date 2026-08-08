convidados = ['Ana', 'Pedro', 'Carlos']

nome = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posicao que deseja inserir esse convidado: "))

#JEITO MAIS DIFICIL
try:
    if convidados[posicao]:
        resto =  list(convidados[posicao-1:])
        while len(convidados[posicao-1:]) > 0:
            convidados.pop()
        convidados.append(nome)
        convidados.extend(resto)
except:
    convidados.append(nome)

print(convidados)

#JEITO MAIS FACIL
if convidados[posicao]:
    convidados.insert(posicao-1, nome)
print(convidados)
