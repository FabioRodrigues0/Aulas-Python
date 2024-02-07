from time import sleep


def contar(i, f, q=1):
    if q == 0:
        q = 1
        if i < f:
            for c in range(i, f + 1, abs(q)):
                print(f'{c}', end=' ')
                sleep(0.3)
        else:
            for c in range(i, f + 1, -abs(q)):
                print(f'{c}', end=' ')
                sleep(0.3)
        print()
    else:
        if i < f:
            for c in range(i, f + 1, abs(q)):
                print(f'{c}', end=' ')
                sleep(0.3)
        else:
            for c in range(i, f + 1, -abs(q)):
                print(f'{c}', end=' ')
                sleep(0.3)
        print()


contar(1, 20, 2)
contar(10, 0, 1)
inicio = int(input('Indique em que numero quer começar: '))
fim = int(input('Indique em que numero quer acabar: '))
qnt = int(input('Indique de quantos em quantos quer contar: '))
contar(inicio, fim, qnt)
