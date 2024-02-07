num = int(input(f'Indique um numero de 0 a 20:\n'))
num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catroze', 'quinze', 'dezaseis', 'dezasete', 'dezoito', 'desanove', 'vinte')
if 0 <= num <= 20:
    print(num_ext[num])
else:
    print('Erro no numero inserido')
