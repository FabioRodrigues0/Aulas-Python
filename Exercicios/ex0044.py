l_num = list()

while True:
    print('Insira novo numero')
    num = int(input(f'->'))
    if l_num.count(num) == 0:
        l_num.append(num)
    op = input('Deseja inserir novo numero [s/n]').strip().upper()
    if op == 'N':
        break
    elif op == 'S':
        continue
    else:
        print('Opção errada')

l_num.sort(reverse=True)
print(l_num)
