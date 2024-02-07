from time import sleep

qnt_25 = 0
qnt_h_17 = 0
qnt_f = 0
qnt_m = 0
opcao = 0

while True:
    print("Deseja inserir um novo registro\n")
    print("[ 1 ] - NOVO REGISTRO")
    print("[ 2 ] - SAIR")

    opcao = int(input("->"))
    idade = 0
    sexo = ''
    if opcao == 1:
        idade = int(input(f"Idade: "))
        sexo = input('Sexo:').strip().upper()
        if idade >= 25:
            qnt_25 += 1
        elif idade < 17 and sexo == 'HOMEM':
            qnt_h_17 += 1
        elif sexo == 'MULHER':
            qnt_f += 1
        elif idade < 18:
            qnt_m += 1
    elif opcao == 2:
        sleep(5)
        print("Obrigado Volte sempre")
        break
    elif 1 >= opcao >= 2:
        print("Opção errada tente outra vez")