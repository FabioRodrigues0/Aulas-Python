from time import sleep

resultado = 0
qnt = 0


def somar(s_num1, s_num2):
    s_resultado = s_num1 + s_num2
    return s_resultado


opcao = 0
maior = 0
menor = 999 * 999

while True:
    print("Deseja inserir outro numero ou sair\n")
    print("[ 1 ] - NOVA NOTA")
    print("[ 2 ] - SAIR")

    opcao = int(input("->"))

    if opcao == 1:
        qnt += 1
        num1 = int(input(f"{qnt} -> "))
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1
        resultado = somar(num1, resultado)
    elif opcao == 2:
        media = resultado / qnt
        print(f'Inserio {qnt} notas dando a media de {media}, sendo que {maior} era a maior nota e {menor} a menor')
        sleep(5)
        print("Obrigado Volte sempre")
        break
    elif 1 >= opcao >= 2:
        print("Opção errada tente outra vez")
