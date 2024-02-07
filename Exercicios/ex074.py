class Livro:
    titulo = str()
    autor = str()

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


l1 = Livro("A Bilia", "Muitos")
l2 = Livro("Os Lusiadas", "Camões")
l3 = Livro("O Verão Passado", "Entre Varios")

print(l1.titulo, " ", l1.autor)
print(l2.titulo, " ", l2.autor)
print(l3.titulo, " ", l3.autor)