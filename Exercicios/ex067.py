from time import sleep


def ver_num(num):
    return num.isnumeric()


while True:
    txt = input('Indique um numero')
    ver = ver_num(txt)
    if ver:
        print('E inteiro')
        sleep(2)
        break
    else:
        print('Erro na intrudução do valor')

