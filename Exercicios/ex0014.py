# Input dos números vindo do utilizador
vel = int(input("Indique um sua velocidade\n"))

multa = 100 + (vel - 80) * 7
if vel > 80:
    print(f"Multado por {multa}")
else:
    print("Não Multado")
