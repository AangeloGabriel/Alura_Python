from armazem.veiculo import Veiculo
from armazem.carro import Carro
from armazem.moto import Moto

def main():
    carro = Carro('Sedan', 'Ferrari', 4)

    moto = Moto('Motocicleta', 'Harley', 'Custom')

    print(carro)
    print(moto)

if __name__ == '__main__':
    main()