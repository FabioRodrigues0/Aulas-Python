def factorial(num, op=False):
    text = ""
    resultado = 1
    for i in range(num, 0, -1):
        resultado = i * resultado

        if i == 1:
            text = text + f"{i}"
        else:
            text = text + f"{i} * "
    if op:
        print(f"{text} =  {resultado}")
    else:
        print(f"{resultado}")


print("Indique um numero:\n")
numero = int(input("-> : "))
while True:
    opcao = input("Deseja imprimir o calculo:\n[ S ] - Sim\n[ N ] - Não ").strip().upper()
    if opcao == 'S' or opcao == 'N':
        if opcao == 'S':
            opcao = True
        else:
            opcao = False
        break
    else:
        print('Opção errada tente outra vez')


factorial(numero, opcao)
