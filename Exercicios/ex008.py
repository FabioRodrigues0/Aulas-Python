# Input dos números vindo do utilizador
km = float(input("Quantos percorreu? "))
dias = int(input("\nQuantos dias alugou? "))

# Variaveis/Calcs
POR_DIA = 60
POR_KM = 0.456
preco = (dias * POR_DIA) + (km * POR_KM)

# Empressão dos dados
print("\nTem que pagar", preco)
