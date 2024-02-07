matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_p = 0
soma_c_2 = 0

print('Indique 9 numeros')
for m in range(0, 3):
    for l in range(0, 3):
        # Input dos números vindo do utilizador
        matriz[m][l] = int(input("->"))

print()
for j, linha in enumerate(matriz):
    for i, elemento in enumerate(matriz[j]):
        print(f'{elemento}', end=' ')
        if (elemento % 2) == 0:
            soma_p = soma_p + elemento
        if i == 1:
            soma_c_2 = soma_c_2 + elemento

    print()

print(soma_p)
print(soma_c_2)
print(max(matriz[2]))
