aluno = dict()
alunos = list()


def inserir():
    notas = list()
    # Input do nome vindo do utilizador
    aluno = {
        'Nome': input('Indique o seu nome:'),
        'Notas': notas}
    # Input dos números vindo do utilizador
    notas.append(float(input("Indique a suas numero notas\n1º:")))

    for x in range(4):
        notas.append(float(input(f"{x + 2}º:")))

    aluno['Notas'] = notas[:]

    notas.clear()

    media = sum(aluno['Notas']) / len(aluno['Notas'])
    aluno['Media'] = media

    alunos.append(aluno)


def escrever_alunos():
    for al in alunos:
        print(f"Nome: {al['Nome']}", end=' ')
        print(f'Notas: ', end='')
        for i, nota in enumerate(al['Notas']):
            if i == 0:
                print(f'{nota}', end='')
            else:
                print(f', {nota}', end='')
        print(f' Media: {al["Media"]}', end=' ')
        if al['Media'] < 9.5:
            print(f" - Reprovado")
        else:
            print(f" - Aprovado")


while True:
    print(f'*' * 40)
    print(f"{'ALUNOS' : ^40}")
    print(f'*' * 40)

    print('Qual das seguindas opçoes deseja fazer:')
    print('[ 1 ] Inserir novo aluno')
    print('[ 2 ] Ver Alunos')
    print('[ 3 ] Sair')

    op = int(input('-> '))

    if op == 1:
        inserir()
    elif op == 2:
        escrever_alunos()
    elif op == 3:
        break
    elif 1 > op > 3:
        print("Opção errada tente outra vez")
