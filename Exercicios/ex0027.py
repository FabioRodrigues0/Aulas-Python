print(f'Indique a Idade de nascimento de 10 pessoas:\n')

alt_nasc = 0
men_nasc = 0

for i in range(1, 11):
    nasc = int(input(f'{i} - '))
    if i == 0:
        alt_nasc = nasc
        men_nasc = nasc
    else:
        if nasc > alt_nasc:
            alt_nasc = nasc
        elif nasc < men_nasc:
            men_nasc = nasc

print(f'Maior: {alt_nasc}\nMenor: {men_nasc}')
