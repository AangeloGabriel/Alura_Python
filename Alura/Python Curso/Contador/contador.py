#GERANDO CONTADOR DE PALAVRAS

# frase = input("Digite uma frase: ")
# palavras = frase.split()
# print(len(palavras))

#GERANDO FUNCAO PARA CONTADOR DE PALAVRAS
def contadorpalavras(texto):
    texto = limpafrase(texto)

    if not texto.strip():
        return {}
    
    palavras = texto.strip()

    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

#GERANDO FUNCAO PARA LIMPAR A FRASE
def limpafrase(frase):
    texto = frase.lower()
    caracteres = ",.!|?;:/()[]@#"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto
