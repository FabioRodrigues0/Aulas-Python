# Imports
import csv
import pandas as pd
# precisa ser instaldo o Pyarrow para o pandas dar
from pathlib import Path

# definiçao de variaveis
path_proj = Path.cwd()
file = f'{path_proj}\\crud\\bd.csv'
header = ['Titulo', 'Autor', 'ISBN', 'Ano', 'Editora', 'Genero', 'Estado', 'Emprestado', 'Data_Devolução']


def add_livro(livro):
    """
    Recebe um dicionário de um livro e faz append ao CSV,
    Se já exitir um livro com o ISBN que esta no livro que está a ser adicionado entao retorna False para
    indicar que falhou a inserção do livro, se for inserto corretamente ele retorna True

    :param livro: dicionário de um livro
    :return: True ou False
    """
    df = pd.read_csv(file)
    rslt_df = df[df['ISBN'] == livro['ISBN']]
    if len(rslt_df) >= 1:
        return False
    else:
        with open(file, 'a', encoding='UTF8', newline='') as t:
            writer = csv.DictWriter(t, fieldnames=header)

            # write the DataBase
            writer.writerow(livro)
        t.close()
        return True


def read_livro():
    dataframe = pd.read_csv(file)
    pd.set_option('display.max_columns', 9)
    return dataframe


def read_livro_param(txt):
    # create a dataframe
    df = pd.read_csv(file)

    # selecting rows based on condition
    rslt_df = df[df['ISBN'] == int(txt)]
    return rslt_df


def read_livro_emp():
    # create a dataframe
    df = pd.read_csv(file)
    pd.set_option('display.max_columns', 9)

    # selecting rows based on condition
    rslt_df = df[df['Estado'] == True]
    return rslt_df


def read_livro_dev():
    # create a dataframe
    df = pd.read_csv(file)
    pd.set_option('display.max_columns', 9)

    # selecting rows based on condition
    rslt_df = df[df['Estado'] == False]
    return rslt_df


def updade_estado_livro(isbn):
    df = pd.read_csv(file)

    update = df[df['ISBN'] == int(isbn)].index
    update_estado = df[df['ISBN'] == int(isbn)].values
    if update.empty:
        txt = f'Livro com {isbn} não existe'
    else:
        df.loc[update, ['Estado']] = not update_estado[0][6]
        txt = f'Livro com {isbn} atualizado com sucesso'
    df.to_csv(file, index=False)
    return txt


def remove_livro(isbn):
    """
    Recebe o ISBN indicado pelo utilizador para procurar o index no CSV do mesmo e o remover
    :param isbn: INT - ISBN
    :return: Sem returno
    """
    # create a dataframe
    df = pd.read_csv(file)
    # Procura o index onde o ISBN e igual ao indicado e da drop
    # axis = 0 significa que o valor que damos antes e index e não coluna
    df.drop(df[df['ISBN'] == int(isbn)].index, axis=0, inplace=True)
    # guarda o ficheiro depois dar o drop
    df.to_csv(file, index=False)
