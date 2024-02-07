from PYTHON.Pacotes.Operaçoes import Operacoes


def calculadora(a, b, c=""):
    if c == Operacoes.SOMA:
        return a + b
    elif c == Operacoes.SUBTRACAO:
        return a - b
    elif c == Operacoes.MULTIPLICACAO:
        return a * b
    elif c == Operacoes.DIVISAO:
        return a / b