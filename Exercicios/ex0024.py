num = int(input(f'Indique um numero:\n'))
if num % 2 == 0 or num % 3 == 0 and num != 3:
    print(f'Numero não é primo')
else:
    print(f'Numero é primo')
