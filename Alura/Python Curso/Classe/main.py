import banco as b

def main():
    conta1 = b.Cliente.criar_conta("Ana", 3400)
    print(conta1)
    
if __name__ == '__main__':
    main()