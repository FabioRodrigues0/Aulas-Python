from datetime import date

print(f'Indique a data de nascimento de 7 pessoas frase:\n')
datas = ['']
qnt = 0
for i in range(1, 8):
    nasc = int(input(f'{i} - '))
    if (date.today().year - nasc) >= 18:
        qnt += 1

print(qnt)
