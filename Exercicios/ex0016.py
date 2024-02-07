# Input dos números vindo do utilizador
num = float(input("Indique a suas numero notas\n1º:"))

for x in range(4):
    num = num + float(input(f"{x + 2}º:"))

media = num / 5

if media < 8:
    print(f"Reprovou com media de {media}")
elif media < 9.5:
    print(f"Em recuperação com media de {media}")
else:
    print(f"Passou com media de {media}")
