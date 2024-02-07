class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite:
            print(f"O seu limite é de {self.limite}€ diarios.")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.saldo} de saldo")
