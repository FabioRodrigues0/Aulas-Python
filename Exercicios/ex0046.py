l_num = list()
p_num = list()
i_num = list()

print('Indique 10 numeros')
for i in range(0, 10):
    # Input dos números vindo do utilizador
    num = int(input("->"))
    l_num.append(num)
    if (num % 2) == 0:
        p_num.append(num)
    else:
        i_num.append(num)

print(f'Lista de Numeros:\n{l_num}')
print(f'Numeros Pares da Lista:\n{p_num}')
print(f'Numeros Impares da Lista:\n{i_num}')