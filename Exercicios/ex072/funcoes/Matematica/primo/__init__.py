def primo(num):
    qnt = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            qnt += 1
        else:
            print('\033[31m', end='')

    if qnt == 2:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo.')