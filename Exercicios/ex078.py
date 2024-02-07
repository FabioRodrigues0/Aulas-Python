class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__pi = 3.14159

    def get_raio(self):
        print(f"O raio é {self.__raio}")

    def set_raio(self, raio):
        self.__raio = raio
        print(f'O Raio foi alterado para {self.__raio}')

    def calc_per(self):
        r = 2 * self.__pi * self.__raio
        print(f'O perimentro do Circulo é {r}')

    def calc_area(self):
        r = self.__pi * (self.__raio * self.__raio)
        print(f'O Area do Circulo é {r}')


cir = Circulo()
cir.get_raio()
cir.set_raio(10)
cir.calc_per()
cir.calc_area()
