from time import sleep

resultado = 0
qnt = 0


def somar(s_num1, s_num2):
    s_resultado = s_num1 + s_num2
    return s_resultado


opcao = 0


while True:
    print("Deseja inserir outro numero ou sair\n")
    print("[ 1 ] - NOVO NUMERO")
    print("[ 2 ] - SAIR")

    opcao = int(input("->"))

    if opcao == 1:
        num1 = int(input("1 -> "))
        qnt += 1
        resultado = somar(num1, resultado)
    elif opcao == 2:
        print(f'Inserio {qnt} dando a soma de {resultado}')
        sleep(10)
        print("Obrigado Volte sempre")
        break
    elif 1 >= opcao >= 2:
        print("Opção errada tente outra vez")

