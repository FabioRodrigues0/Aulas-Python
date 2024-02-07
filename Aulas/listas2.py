turma = list()
aluno = list()

for c in range(0, 3):
    aluno.append(input('Digite o nome do aluno: '))
    aluno.append(int(input('Digite a idade: ')))
    turma.append(aluno[:])
    aluno.clear()

print(turma[0])

for i in turma:
    print(f'i:{i}')

