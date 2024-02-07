import datetime

pessoa = {
    'Nome': input('Indique o nome: '),
    'Ano': int(input('Indique o Ano de Nascimento: ')),
    'Rendimentos': float(input('Indique os rendimentos mensais: ')),
    'Despesas': float(input('Indique as despesas mensais: ')),
    'Credito': float(input('Indique o montante a credito: ')),
    'Prazo': int(input('Indique o prazo do credito em mes: '))
}
pessoa['Idade'] = datetime.date.today().year - pessoa['Ano']
pessoa['Remanescente'] = pessoa['Rendimentos'] - pessoa['Despesas']
pessoa['Mes'] = pessoa['Credito'] / pessoa['Prazo']

if pessoa['Remanescente']> pessoa['Mes']:
    print('Aprovado')
else:
    print('Reprovado')
