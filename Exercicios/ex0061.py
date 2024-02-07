def ver_maior(*num):
    print(f'O maior numero que indicou é {max(num[0])}')
    print()


txt = input('Indique varios numeros separados por espaço: ').strip().split()
ver_maior(txt)
