import header
import calc


header.header("Calculadora Mágica")
# programa principal
num1 = int(input('Digite o primeiro número'))
num2 = int(input('Digite o segundo número'))

print(f"A som entren {num1} e {num2} é igual a {calc.calc(num1, num2)}")
