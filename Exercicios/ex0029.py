import random

opcao = 1
# Input dos números vindo do utilizador
print('Indique 1º numero de 0 a 10 : ')
while opcao == 1:
    num1 = int(input("--->"))
    num2 = random.randint(0, 10)
    # ‘set’ de condições para determinar para que formato e para converter
    if num1 == num2:
        print(f"Utilizador Ganhou")
        opcao = 2
    else:
        print(f"Utilizador Perdeu")
        print('tente novamente')
