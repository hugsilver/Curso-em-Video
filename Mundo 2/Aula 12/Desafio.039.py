
from datetime import date
data_atual_ano = date.today().year

year = int(input('Digite sua data de nascimento: '))
print('Considerando a data atual {}'.format(data_atual_ano))

if (data_atual_ano - year) >18:
    print('Já passou da hora, Corno.')
    print('Passou {} do alistamento.'.format((data_atual_ano - year)-18))
elif(data_atual_ano - year) <18:
    print('Calma, ainda vai se fuder.')
    print('Faltam {} anos para o alistamento.'.format(18 - (data_atual_ano - year)))
else:
    print('Se Fudeo, tem que se alistar.')


