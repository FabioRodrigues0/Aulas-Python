import random

# criação e iniciação das variavies
chaves = list()
qnt = int(input('Quantas Chaves quer gerar?\n-> '))

# gerar as chaves
for i in range(0, qnt):
    chaves.append([random.sample(range(1, 51), 5), random.sample(range(1, 13), 2)])

for chave in chaves:
    print('Nº: ', end='')
    for num in sorted(chave[0]):
        print(f'{num}', end='')
    print('*: ', end='')
    for estrela in sorted(chave[1]):
        print(f'{estrela}', end=' ')
    print()

