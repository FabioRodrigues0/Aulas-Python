import random
from time import sleep

qnt = 0
while True:
    # Input dos números vindo do utilizador
    num_p = int(input("Indique um numero de 0 a 10\n"))
    num_pc = random.randint(0, 10)
    soma = num_p + num_pc

    print("[ 1 ] - PAR")
    print("[ 2 ] - IMPAR")

    opcao = int(input("->"))

    if opcao == 1 and (soma % 2) == 0:
        qnt += 1
    elif opcao == 2 and not (soma % 2) == 0:
        qnt += 1
    else:
        print("Perdeu\n")
        print(f'Escolheu {num_p} e computador {num_pc} que a sua soma é {soma}')
        print(f'Teve {qnt} vitorias')
        sleep(3)
        break

