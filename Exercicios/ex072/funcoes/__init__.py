import Matematica.Matematica as m
import Matematica.Operaçoes as op


def call_calc():
    conta = input('Indique a conta que deseja fazer separada por espaços:\n-> ').lower().strip().split(' ')

    if conta[3] == "+":
        m.calc(conta[1], conta[3], op.Operacoes.SOMA)
    elif conta[3] == "x":
        m.calc(conta[1], conta[3], op.Operacoes.MULTIPLICACAO)
    elif conta[3] == "/":
        m.calc(conta[1], conta[3], op.Operacoes.DIVISAO)
    elif conta[3] == "-":
        m.calc(conta[1], conta[3], op.Operacoes.SUBTRACAO)
