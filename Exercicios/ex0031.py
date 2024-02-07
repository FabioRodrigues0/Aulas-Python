print("Indique um numero:\n")
num = int(input("1º: "))
text = ""
resultado = 1
for i in range(num, 0, -1):
    resultado = i * resultado

    if i == 1:
        text = text + f"{i}"
    else:
        text = text + f"{i} * "

print(f"O factorial do numero {num} é:\n{text} =  {resultado}")
