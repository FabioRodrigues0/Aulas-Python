import random


def somar(s_num1, s_num2, s_num3):
    resultado = s_num1 + s_num2 + s_num3
    print(f"O resultado da soma dos numeros é\n {s_num1} + {s_num2} + {s_num3} = {resultado}")


def multi(m_num1, m_num2, m_num3):
    resultado = m_num1 * m_num2 * m_num3
    print(f"O resultado da multiplicação dos numeros é\n {m_num1} x {m_num2} x {m_num3} = {resultado}")


def maior(mr_num1, mr_num2, mr_num3):
    if mr_num1 > mr_num2 and mr_num1 > mr_num3:
        print("O primeiro numero e o maior")
    elif mr_num2 > mr_num1 and mr_num2 > mr_num3:
        print("O segundo numero e o maior")
    elif mr_num3 > mr_num1 and mr_num3 > mr_num2:
        print("O terceiro numero e o maior")


def novos():
    n_num1 = random.randint(0, 100)
    n_num2 = random.randint(0, 100)
    n_num3 = random.randint(0, 100)
    print(f"Os novos numeros gerados são:\n{n_num1}\n{n_num2}\n{n_num3}")


opcao = 0

while opcao < 5:
    print(f'Indique 3 numeros de 0 a 100\n')

    num1 = int(input("1º: "))
    num2 = int(input("2º: "))
    num3 = int(input("3º: "))

    print("Indique o pretende fazer com esses numeros\n")
    print("[ 1 ] - SOMAR")
    print("[ 2 ] - MULTIPLICAR")
    print("[ 3 ] - MAIOR")
    print("[ 4 ] - NOVOS")
    print("[ 5 ] - SAIR")

    opcao = int(input("->"))

    if opcao == 1:
        somar(num1, num2, num3)
    elif opcao == 2:
        multi(num1, num2, num3)
    elif opcao == 3:
        maior(num1, num2, num3)
    elif opcao == 4:
        novos()
    elif 1 > opcao > 5:
        print("Opção errada tente outra vez")
