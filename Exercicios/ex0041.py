print("Insira 4 Numeros")

a = input(f'->')
b = input(f'->')
c = input(f'->')
d = input(f'->')

t_num = (a, b, c, d)
print(t_num)
print(f'O numero 7 apareceu {t_num.count('7')}')
if t_num.count('5') == 1:
    print(f'O numero 5 foi digitado na posição {t_num.index('5')} ')
else:
    print('Não digitou nenhuma vez o numero 5')

print(f'Os numeros pares são', end='')
for i in range(0, len(t_num)):
    if int(t_num[i]) % 2 == 0:
        print(f',{t_num[i]} ', end='')
