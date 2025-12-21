
import datetime
#Poderia ser from datetime import date

cont1 = 0
cont2 = 0

for i in range(1, 8, 1):
    dat = int(input('Digite a data de nascimento da {} pessoa: '.format(i)))
    ano_atual = datetime.date.today().year
    if((ano_atual - dat)>=21):
        cont1 += 1
    else:
        cont2 += 1

print('{} pessoas são maiores de idade.'.format(cont1))
print('{} pessoas são memores de idade.'.format(cont2))

#Posso colocar uma validação da data para datas acima de do ano atula nãos erem contadas .




