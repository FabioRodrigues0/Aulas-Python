from crud.listar import listagem
from crud.gestor import read_livro_emp, updade_estado_livro


def emprestar_livro():
    lista = read_livro_emp()
    listagem(lista)
    isbn_emprestimo = input("Digite o ISBN do livro a ser emprestado: ")
    result = updade_estado_livro(isbn_emprestimo)
    print(result)

