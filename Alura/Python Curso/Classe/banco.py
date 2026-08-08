class ContaBancaria:
    def __init__(self, titular = '', saldo = 0):
        self.titular = titular  
        self.saldo = float(saldo)
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo}'
    
    def ativar_conta(self):
        self._ativo = True

class Cliente:
    @classmethod
    def criar_conta(cls, nome, valor):
        conta = ContaBancaria(nome, valor)
        return conta


