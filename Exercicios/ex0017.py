# Input dos números vindo do utilizador
num = int(input("Indique numero:"))
opcao = int(input("Para que formato quer converter\n1 - Binario\n2 - Octal\n3 - Hexadecimal\n"))

# ‘set’ de condições para determinar para que formato e para converter
if opcao == 1:
    text = str(bin(num))
    text = text.replace("0b", "")
    print(f"O numero que indicou em binario é {text}")
elif opcao == 2:
    # a impressao usando o range
    print(f"O numero que indicou em Octal é {oct(num)[2:]}")
elif opcao == 3:
    text = str(hex(num))
    text = text.replace("0h", "")
    print(f"O numero que indicou em Hexadecimal é {text}")
else:
    print("Para proxima insere um opção correta")
