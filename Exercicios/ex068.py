aluno = dict()
alunos = list()


def cabecalho():
    print(f'*' * 40)
    print(f"{'ALUNOS' : ^40}")
    print(f'*' * 40)


def menu():
    print('Qual das seguindas opçoes deseja fazer:')
    print('[ 1 ] Inserir novo aluno')
    print('[ 2 ] Ver Alunos')
    print('[ 3 ] Resumo Turma')
    print('[ 4 ] Sair')


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


def resumo_turma():
    soma = 0
    m_nota = 0
    print(f'A quantidade de Alunos registrados é {len(alunos)}')
    for a in alunos:
        t_nota = max(a['Notas'])
        m_nota = t_nota if t_nota > m_nota else m_nota
        soma = soma + a['Media']
    print(f'A nota mais alta é {m_nota}')
    print(f'A media da turma é {soma / len(alunos)}')


while True:
    cabecalho()
    menu()

    op = int(input('-> '))

    if op == 1:
        inserir()
    elif op == 2:
        escrever_alunos()
    elif op == 3:
        resumo_turma()
    elif op == 4:
        break
    elif 1 > op > 4:
        print("Opção errada tente outra vez")
