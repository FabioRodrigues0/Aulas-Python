while True:
    try:
        num1 = int(input('Indique o primeiro numero:'))
        num2 = int(input('Indique o segundo numero:'))
        r = num1 / num2
    except ZeroDivisionError:
        print('Um numero não pode ser divisivel por 0')
    except ValueError:
        print('Os valores inseridos são invalidos')
    else:
        break


