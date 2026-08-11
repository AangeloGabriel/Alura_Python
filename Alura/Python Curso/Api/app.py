import requests 

url ='https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print(f'O erro foi {response.status_code}')