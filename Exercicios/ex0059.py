def cabecalho(msg):
    print('-=' * (len(msg) + 3))
    print(f'{msg: ^{2 * len(msg) + 6}}')
    print('-=' * (len(msg) + 3))
    print()


cabecalho('Ola')