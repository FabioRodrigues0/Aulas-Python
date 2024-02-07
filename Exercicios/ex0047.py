print('Indique uma Equação')
eq = input('Equação: ')

if eq.count('(') == eq.count(')'):
    print('Equação esta correta')
else:
    print('Equeção esta incorreta')
