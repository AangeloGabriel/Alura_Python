from abc import ABC, abstractmethod
class Veiculo(ABC):

    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self._ligado = False
        self._buzina = False

    def __str__(self):
        return f"Modelo do veiculo: {self.modelo} | Marca do veiculo: {self.marca} | Estado: {self.estado()} | Buzina {self._buzina}"

    def estado(self):
        if self._ligado:
            return 'Ativo'
        else:
            return 'Inativo'

    @abstractmethod
    def buzina(self):
        self._buzina = True