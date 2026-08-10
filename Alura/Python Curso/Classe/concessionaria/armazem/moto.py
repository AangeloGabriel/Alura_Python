from armazem.veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, modelo, marca, tipo):
        super().__init__(modelo, marca)
        self.tipo = tipo

    def __str__(self):
        return f"Modelo do veiculo: {self.modelo} | Marca do veiculo: {self.marca} | Tipo do veiculo: {self.tipo} | Estado: {self.estado()} | Buzina {self._buzina}"

    def buzina(self):
        self._buzina = True