

tupla_times = ('Palmeiras' , 'Flamengo' , 'Cruzeiro', 'Mirassol', 'Botafogo', 'Bahia', 'FLuminense', 'São Paulo', 'Bragantino', 'Ceará SC', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')
#Para testar com chapecoense
#tupla_times = ('Palmeiras' , 'Cruzeiro', 'Mirassol', 'Botafogo', 'Chapecoense', 'Bahia', 'FLuminense', 'São Paulo', 'Bragantino', 'Ceará SC', 'Vasco da Gama', 'Corinthians', 'Grêmio', 'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')


print(tupla_times)

print('Os 5 primeiros colocados são: ')
print(tupla_times[0:5])

print('Os 4 ultimos colocados são: ')
print(tupla_times[-4:])

print('Times em Ordem AlfaBética: ')
print(sorted(tupla_times))

#Utilizar método index

if 'Chapecoense' in tupla_times:
    print(f'O time chapecoense esta na posição {tupla_times.index('Chapecoense') +1 } dos classificados')
else:
    print(f'Chapecoense não está entre os {len(tupla_times)} classificados')

