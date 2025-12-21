

'''
from datetime import datetime

person = dict()
ano_atual = datetime.now().year

person['nome'] = str(input('Digite o nome da pessoa: '))
person['year_born'] = int(input('Digite o ano de nascimento da pessoa: '))
person['CTPS'] = int(input('Digite a CTPS da pessoa: '))
idade = ano_atual - person['year_born']
men = 35
mulher = 30
person['idade'] = idade

if person['CTPS'] != 0:
    person['year_contract'] = int(input('Digite o ano de contratação da pessoa: '))
    person['sold'] = float(input('Digite o sálario da pessoa: '))
    person['idade'] = idade
    person['id_aposent_men'] = men + person['year_contract']
    person['id_aposent_woman'] = mulher + person['year_contract']
    print(f'Olá {person['nome']}, você nasceu em {person['year_born']}, atualmente tem {person['idade']} anos, se for homem irá se aposentar com {person['id_aposent_men']} , se for mulher irá se aposentar com {person['id_aposent_woman']}')
    print('Considerando somente o tempo de contribuição mínimo, de 30 anos para mulheres e 35 para homens!!!')

else:
    print(f'Os seus dados são: Nome: {person['nome']}, nascido em {person['year_born']} com idade de {person['idade']} anos e CTPS: {person['CTPS']}')
'''


#Metodo Guana

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Digite o nome da pessoa: '))
nasc =  int(input('Digite o ano de nascimento da pessoa: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] =  int(input('Digite a CTPS da pessoa (0 não tem): '))

if dados['CTPS'] != 0:
    dados['contra'] = int(input('Ano de contratação: '))
    dados['sal'] =  float(input('Salario: R$ '))
    dados['aposenta'] = (dados['contra'] + dados['idade'] + 35 - datetime.now().year)


print(dados)


