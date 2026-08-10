from armazem.veiculo import Veiculo
from armazem.carro import Carro
from armazem.moto import Moto

def main():
    carro = Carro('Sedan', 'Ferrari', 4)
    print(carro)
    carro.buzina()
    print(carro)

    moto = Moto('Motocicleta', 'Harley', 'Custom')

    print(moto)

if __name__ == '__main__':
    main()