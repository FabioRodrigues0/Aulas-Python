linha = list()
elem = list()

print('Indique 9 numeros')
for m in range(0, 3):
    for l in range(0, 3):
        # Input dos números vindo do utilizador
        elem.append(int(input("->")))
    linha.append(elem[:])
    elem.clear()

print()
for l in linha:
    for elemento in l:
        print(f'{elemento}', end=' ')
    print()
