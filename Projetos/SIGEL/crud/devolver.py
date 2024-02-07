from crud.listar import listagem
from crud.gestor import read_livro_dev, updade_estado_livro


def devolucao_livro():
    lista = read_livro_dev()
    listagem(lista)
    isbn_devolucao = input("Digite o ISBN do livro a ser devolvido: ")
    updade_estado_livro(isbn_devolucao)
