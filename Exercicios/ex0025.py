text = input(f'Indique uma frase:\n').lower().strip().replace(' ', '')
text_inv = text[::-1]

if text == text_inv:
    print(f'A frase que indicou é palíndromo\n1 - {text}\n2 - {text_inv}')
else:
    print(f'A frase que indicou não é palíndromo\n1 - {text}\n2 - {text_inv}')
