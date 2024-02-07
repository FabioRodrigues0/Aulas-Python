import random
list_num = list()
for i in range(0, 5):
    list_num.insert(i, random.randint(0, 100))

t_num = tuple(list_num)
print(f'O maior numero na lista gerada é {max(t_num)}')
print(f'O menor Numero da lista gerada é {min(t_num)}')
print(list_num)
