import datetime


def ver_pessoa(ano):
    """
    Função em que verifica se uma pessoa pode ou não ter carta
    :param ano:
    :return : Um texto com a indicaçao se pode ou não tirar a carta
    """
    idade = datetime.date.today().year - ano
    if idade >= 18:
        return 'Pode'
    elif 18 > idade >= 16:
        return 'Pode mas com Autorização'
    else:
        return 'Não pode'


resposta = ver_pessoa(int(input('Digite o ano em que nasceu: ')))
print(resposta)
