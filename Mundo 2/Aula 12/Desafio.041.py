
from datetime import date

data_atual = date.today().year

year = int(input('Digite o ano do seu nascimento: '))

ano = data_atual - year

if ano <=9:
    print('Categoria MIRIM.')
elif ano > 9 and ano <=14 :
    print('Categoria INFANTIL.')
elif ano >14 and ano <=19 :
    print('Categoria JUNIOR.')
elif ano > 19 and ano <= 20 :
    print('Categoria SêNIOR.')
else:
    print('Categoria MASTER.')













