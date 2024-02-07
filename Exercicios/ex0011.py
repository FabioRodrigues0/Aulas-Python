# Input dos números vindo do utilizador
text = input("Indique uma frase\n").lower()

# Empressão dos dados
print(f"Quantas vezes aparece Letra A : {text.count("a")}")
print(f"Posição da primeira Letra A : {text.find("a") + 1}")
print(f"Posição da Ultima Letra A : {text.rfind("a") + 1}")
