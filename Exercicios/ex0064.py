def convert_far(num):
    far = (num * 9 / 5) + 32
    print(f'A temperatura de {num} em Fahrenheit é {far}')


print('~' * 20)
print('Converção em Fahrenheit')
print('~' * 20)

numero = float(input(f'Indique a temperatura em Celsius:\n'))
convert_far(numero)
