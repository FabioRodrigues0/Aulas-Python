# Input dos números vindo do utilizador
nome = input("Indique o seu nome\n").lower().strip()
nome = nome.split()
email = "{}.{}.edu@empresa.pt".format(nome[0][0], nome[1])
print("Olá {}, o seu registo está completo.".format(nome[0]))
print("O seu email é {}".format(email))
