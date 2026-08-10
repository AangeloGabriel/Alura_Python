from armazem.veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo, marca, portas):
        super().__init__(modelo, marca)
        self.portas = portas

    def __str__(self):
        return f"Modelo do veiculo: {self.modelo} | Marca do veiculo: {self.marca} | Estado: {self.estado()} | Portas: {self.portas} | Buzina {self._buzina}"

    def buzina(self):
        self._buzina = True