print('Insira 5 numeros')
l_num = list()
for i in range(0, 5):
    if len(l_num) == 0:
        l_num.append(int(input(f'->')))
    else:
        num = int(input(f'->'))
        if num <= l_num[-1]:
            for j, v in enumerate(l_num):
                if v < num < l_num[(j + 1) % len(l_num)]:
                    l_num.insert(j + 1, num)
                    break
                elif num < v:
                    l_num.insert(j - 1, num)
                    break
        else:
            l_num.append(num)

print(l_num)