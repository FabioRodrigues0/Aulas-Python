def tabuada(num):
    for c in range(0, 10):
        print(f'{num} x {c + 1} = {(c + 1) * num}')


def par_impar(num):
    if (num % 2) == 0:
        print('Numero e Par')
    else:
        print('Numero e Impar')