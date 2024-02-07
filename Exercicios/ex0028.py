from time import sleep

print(f'VERDADEIRO ou FALSO\n\n')
opcao = 0
while opcao < 3:
    # pergunta e resposta
    perguntas = ['Está a chover hoje?', 'A centopeia tem 100 patas?', 'O Cesar esta com sono?']
    respostas = ['F', 'V', 'V']

    resposta = input(perguntas[opcao]).strip().upper()
    if resposta == respostas[opcao]:
        print('Correto!')
        sleep(3)
        print('Proxima pergunta')
        opcao += 1
    elif resposta != respostas[opcao]:
        print('Errado')
        sleep(3)
        print('Tente novamente')
    else:
        print('Erro!\nIndique:\n[ V ]\n[ F ]')
print('Obrigado volte sempre.')
