class Veiculo:

    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self._ligado = False

    def __str__(self):
        return f"Modelo do veiculo: {self.modelo} | Marca do veiculo: {self.marca} | Estado: {self.estado()}"

    def estado(self):
        if self._ligado:
            return 'Ativo'
        else:
            return 'Inativo'
