# Imports
from crud.gestor import read_livro, remove_livro


def apagar_livro():
    biblioteca = read_livro()
    print(biblioteca)
    apaga_isbn = input("Indique o ISBN do livro que pretende apagar: ")
    remove_livro(apaga_isbn)
