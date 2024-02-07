print('Insira 5 numeros')
l_num = list()
for i in range(0, 5):
    l_num.append(int(input(f'Nº{i+1} :')))

print(f'O Maior numero inserido foi {max(l_num)} e a sua posiçao foi {1 + l_num.index(max(l_num))}')
print(f'O Menor numero inserido foi {min(l_num)} e a sua posiçao foi {1 + l_num.index(min(l_num))}')