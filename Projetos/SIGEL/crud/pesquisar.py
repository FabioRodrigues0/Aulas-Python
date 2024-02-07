from crud.gestor import read_livro_param


def pesquisa():
    isbn = input('Indique o ISBN que pretende procurar:')
    biblioteca = read_livro_param(isbn)
    print(biblioteca)
