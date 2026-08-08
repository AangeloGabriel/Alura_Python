class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #metodo especial
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #Botando cada restaurante no restaurantes

    def __str__(self):  #metodo especial
        return f'Restaurante: {self.nome} \nCategoria: {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')



restaurante_praca = Restaurante('Joses', 'Gourmet')

# print(vars(restaurante_praca))
# print(restaurante_praca)

Restaurante.listar_restaurantes()
