# Imports
import os
import re

from crud.gestor import add_livro


def adicionar_livro():
    opcao = "S"
    while opcao == "S":
        # limpa consola
        os.system("cls")
        # inicia as listas e o dicionario
        autor = list()
        genero = list()
        livros = dict()

        # inputs e adiciona ao dicionario , no caso dos parametros que podem ter mais
        livros["Titulo"] = input("Titulo: ")
        opcao = "S"
        # adiciona autores à  ate o user nao pretender adicionar mais e depois adiciona a lista ao dicionario
        while opcao == "S":
            autor.append(input("Autor: "))
            opcao = input("Deseja inserir mais autores ? [S/N]").strip().upper()
        if len(autor) >= 2:
            livros["Autor"] = ", ".join(genero[:])
        else:
            livros["Autor"] = "".join(genero[:])
        autor.clear()
        while True:
            txt = input("ISBN: ")

            if re.search("^(978[0-9].{1,3}[0-9].{2,7}[0-9][0-9])", txt):
                livros["ISBN"] = txt
                break
            else:
                print("Insira um ISBN válido")

        livros["Ano"] = int(input("Ano: "))
        livros["Editora"] = input("Editora: ")
        opcao = "S"
        # adiciona generos ate o user nao pretender adicionar mais e depois adiciona a lista ao dicionario
        while opcao == "S":
            genero.append(input("Genero: ").strip().upper())
            opcao = input("Deseja inserir mais Generos ? [S/N]").strip().upper()
        if len(genero) >= 2:
            livros["Genero"] = ", ".join(genero[:])
        else:
            livros["Genero"] = "".join(genero[:])
        genero.clear()
        # Por definição ao adicionar um livro ele fica disponivel
        livros["Estado"] = True
        result = add_livro(livros)
        if result:
            print("Book inserido com sucesso")
        else:
            print("Já existe um livro com esse ISBN\nPor favor confirme os dados")
