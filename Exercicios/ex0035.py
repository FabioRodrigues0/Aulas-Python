print('~' * 20)
print('Tabuada')
print('~' * 20)


while True:
    num = int(input(f'Indique um numero:\n'))
    if num >= 1:
        for c in range(0, 10):
            print(f'{num} x {c + 1} = {(c + 1) * num}')
    else:
        break
