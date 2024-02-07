from crud.gestor import read_livro


def listagem(lista=None, ):
    if lista is None:
        biblioteca = read_livro()
        # print("Titulo | Autor | ISBN | Ano | Editora | Genero | Disponibilidade | Emprestado | Data_Devolução")
        print(biblioteca)
    else:
        print(lista)

