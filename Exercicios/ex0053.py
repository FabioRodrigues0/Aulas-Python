import random

from operator import itemgetter

nomes = ['Joao', 'Ana', 'Luis', 'Joana']
jogador = dict()
jogadores = list()

for i in range(0, 4):
    jogador = {
        "Nome": nomes[i],
        "Dado": random.randint(1, 7)
    }
    jogadores.append(jogador)

print(f'*' * 40)
print(f"{'RANKING' : ^40}")
print(f'*' * 40)

sorted(jogador, key=itemgetter(2))
for j in jogadores:
    print(f"{j['Nome']} -  {j['Dado']}")
