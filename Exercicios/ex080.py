class Alunos:
    __alunos = list()

    def __init__(self):
        pass

    def get_alunos(self):
        return self.__alunos

    def set_alunos(self, valor):
        self.__alunos.append(valor)


class Aluno:
    def __init__(self):
        self.__nome = "NOME_ALUNO"
        self.__notas = list()
        self.__media = len(self.__notas)

    def get_nome_aluno(self):
        return self.__nome

    def set_nome_aluno(self, valor):
        self.__nome = valor

    def get_notas_aluno(self):
        return self.__nome

    def set_notas_aluno(self, valor):
        self.__notas = valor[:]

    def get_media_aluno(self):
        return self.__media

    def set_media_aluno(self):
        self.__media = sum(self.__notas) / len(self.__notas)


def inserir():
    notas = list()
    # Input do nome vindo do utilizador
    txt = input('Indique o seu nome:'),
    aluno.set_nome_aluno(txt)
    # Input dos números vindo do utilizador
    notas.append(float(input("Indique a suas numero notas\n1º:")))

    for x in range(4):
        notas.append(float(input(f"{x + 2}º:")))

    aluno.set_notas_aluno(notas)

    notas.clear()

    aluno.set_media_aluno()
    alunos.set_alunos(aluno)


def escrever_alunos():
    list_alunos = alunos.get_alunos()
    for al in list_alunos:
        print(f"Nome: {al._Aluno__nome[0]}", end=' ')
        print(f'Notas: ', end='')
        for i, nota in enumerate(al._Aluno__notas):
            if i == 0:
                print(f'{nota}', end='')
            else:
                print(f', {nota}', end='')
        print(f' Media: {al._Aluno__media}', end=' ')
        if al._Aluno__media < 9.5:
            print(f" - Reprovado")
        else:
            print(f" - Aprovado")


while True:
    aluno = Aluno()
    alunos = Alunos()

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