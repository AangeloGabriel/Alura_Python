from fastapi import FastAPI, Query
import requests

app = FastAPI()

"""
Para iniciar uma API colcoar no terminal de comandos
uvicorn main:app
"""

@app.get('/api/hello')
def hello_world():
    """
    Gerador de Hello Word Nessa bagaça
    """
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    # Para acessar o restaurante em especifico colocar /api/restaurantes/?restaurante=RESTAURANTE
    
    url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append(
                    {
                    "item":         item['Item'],
                    "preco":        item['price'],
                    "description":  item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}