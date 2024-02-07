import random

opcao = input(f"Vamos Jogar ao Pedra, Papel, Tessoura?\nS - Sim\nN - Não\n")
if opcao == 'S' or opcao == 's':
    # Input da escolha vindo do utilizador
    print('Escolha umas das opções:')
    escolha = int(input("Jogue\n[ 1 ] - Pedra\n[ 2 ] - Papel\n[ 3 ] - Tesoura\n"))
    escolha_rand = random.randint(1, 3)
    if (escolha == 1 and escolha_rand == 2) or (escolha == 2 and escolha_rand == 3) or (
            escolha == 3 and escolha_rand == 1):
        print(f"Utilizador Perdeu")
    elif (escolha == 1 and escolha_rand == 3) or (escolha == 3 and escolha_rand == 3) or (
            escolha == 2 and escolha_rand == 1):
        print(f"Utilizador Ganhou")
    elif escolha == escolha_rand:
        print(f"Utilizador Empatou")
    else:
        print(f"Escolheu a opção errada")
elif opcao == 'N' or opcao == 'n':
    print(f"Obrigado volte sempre")
else:
    print(f"Escolheu a opção errada")
