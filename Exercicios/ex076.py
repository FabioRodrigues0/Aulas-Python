class Produto:
    nome = str()
    qnt_stock = float()

    def __init__(self, nome, qnt_stock):
        self.nome = nome
        self.qnt_stock = qnt_stock

    def __str__(self):
        return self.nome + " " + str(self.qnt_stock)


class ListProduto:
    lista = list()

    def __init__(self):
        pass

    def add_to_lista(self, nome, qnt_stock):
        self.lista.append(Produto(nome, qnt_stock))

    def get_lista(self):
        return self.lista


obj_list = ListProduto()
obj_list.add_to_lista("Maça", 20)
obj_list.add_to_lista("Perâ", 5)
lista_produtos = obj_list.get_lista()
for p in lista_produtos:
    print(p)
