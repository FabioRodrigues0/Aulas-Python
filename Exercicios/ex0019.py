import random

# Input dos números vindo do utilizador
num1 = int(input("Indique 1º numero : "))
num2 = random.randint(0, 7)

# ‘set’ de condições para determinar para que formato e para converter
if num1 == num2:
    print(f"Utilizador Ganhou")
else:
    print(f"Utilizador Perdeu")
