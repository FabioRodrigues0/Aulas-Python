l_num = [[],[]]

print('Indique 10 numeros')
for i in range(0, 10):
    # Input dos números vindo do utilizador
    num = int(input("->"))
    if (num % 2) == 0:
        l_num[0].append(num)
    else:
        l_num[1].append(num)

print(f'Lista de Numeros:\n{l_num}')
print(f'Numeros Pares da Lista:\n{sorted(l_num[0])}')
print(f'Numeros Impares da Lista:\n{sorted(l_num[1])}')