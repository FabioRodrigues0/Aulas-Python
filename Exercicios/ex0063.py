def printt_tabuada(num):
    for c in range(0, 10):
        print(f'{num} x {c + 1} = {(c + 1) * num}')


print('~' * 20)
print('Tabuada')
print('~' * 20)


numero = int(input(f'Indique um numero:\n'))
printt_tabuada(numero)
