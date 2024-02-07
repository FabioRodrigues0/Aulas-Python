class Livro:
    def __init__(self):
        self.__titulo = str()
        self.__ano = int()
        self.__autor = str()
        self.__estado = bool()

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, t):
        self.__titulo = t

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, a):
        self.__ano = a

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, a):
        self.__autor = a

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, e):
        self.__estado = e


print(f"{'BIBLIOTECA' : ^40}")
print(f'*' * 40)

titulo = input('Indique o titulo do livro: ').strip()
ano = int(input('Indique o ano do livro: ').strip())
autor = input('Indique o autor do livro: ').strip()
estado = input('Indique a disponibilidade do livro: ').strip().lower()
if estado == 's':
    estado = True
else:
    estado = False

livro = Livro()
livro.titulo = titulo
livro.ano = ano
livro.autor = autor
livro.estado = estado
print(livro.titulo)
print(livro.ano)
print(livro.autor)
print(livro.estado)
