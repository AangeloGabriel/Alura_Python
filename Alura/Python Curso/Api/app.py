import requests
import json
import os 

local_atual = os.getcwd()
pasta = 'Restaurantes'

novo_local_pasta = os.path.join(local_atual, pasta)

os.makedirs(novo_local_pasta, exist_ok=True)

url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    
    for item in dados_json:
        nome_do_restaurante = item['Company']
        
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        else:
            dados_restaurante[nome_do_restaurante].append(
                {
                "item":         item['Item'],
                "preco":        item['price'],
                "description":  item['description']
                
            })

else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{os.path.join(novo_local_pasta,nome_do_restaurante)}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4, )
