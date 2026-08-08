# Uma escola está organizando os dados dos alunos para criar 
# um relatório resumido. Cada aluno tem seus dados registrados 
# em uma única entrada, incluindo nome, idade e nota final no 
# semestre. Esses dados devem ser exibidos separadamente para 
# cada aluno no formato abaixo:

# Aluno: Nome
# Idade: Idade
# Nota: Nota

# João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

alunos = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").strip().split(',')

for i in range(0, len(alunos), 3):
    print("Nome: ", alunos[i])
    print("Idade: ", alunos[i+1])
    print("Nota: ", alunos[i+2])
    print("")
