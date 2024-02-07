class Conta:
    def __init__(self, nib, titular):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = 0
        self.__limite = 1000

    def get_conta(self):
        print(f'Conta\nNIB = {self.__nib}\nTITULAR = {self.__titular}\nSALDO = {self.__saldo}\nLIMITE = {self.__limite}')

    def get_nib(self):
        print(f'NIB: {self.__nib}')

    def set_nib(self, valor):
        self.__nib = valor
        print(f'NIB: {self.__nib}')

    def get_titular(self):
        print(f'TITULAR: {self.__titular}')

    def set_titular(self, valor):
        self.__titular = valor
        print(f'TITULAR: {self.__titular}')

    def get_saldo(self):
        print(f'SALDO: {self.__saldo}')

    def set_saldo(self, valor):
        self.__saldo = valor
        print(f'SALDO: {self.__saldo}')

    def get_limite(self):
        print(f'LIMITE: {self.__limite}')

    def set_limite(self, valor):
        self.__limite = valor
        print(f'LIMITE: {self.__limite}')

    def levantar(self, valor):
        if valor > self.__limite:
            print(f"O seu limite é de {self.__limite}€ diarios.")
        else:
            if self.__saldo > valor:
                self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f"A conta {self.__nib} tem {self.__saldo} de saldo")


c = Conta('21344122', 'Fábio')
c.get_saldo()
c.set_saldo(1000)
c.get_limite()
c.levantar(500)
c.depositar(40)
c.extrato()
