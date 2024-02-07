# Input dos números vindo do utilizador
num1 = int(input("Indique 1º numero : "))
num2 = int(input("Indique 2º numero : "))

# ‘set’ de condições para determinar para que formato e para converter
if num1 == num2:
    print(f"Os numeros que indicou são iguais")
elif num1 < num2:
    # a impressao usando o range
    print(f"O segundo numero que indicou é maior")
else:
    print(f"O primeiro numero que indicou é maior")
