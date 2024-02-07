def cabecalho(msg):
    print('-=' * 20)
    print(msg)
    print('-=' * 20)
    print()


def calc_area(largura, comprimento):
    print(f'A area do terreno é {largura * comprimento}m2')


cabecalho('Exercicio 58 - Area')
alt = int(input('Indique a largura do terreno em metros:'))
comp = int(input('Indique o comprimento do terreno em metros:'))
calc_area(alt, comp)



