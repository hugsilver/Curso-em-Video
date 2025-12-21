
tupla_it_var = ('Processador i9',5600,'Placa Mãe - Aourus',2500,'Gabinete',2000,'RAM',2000,'SSD',800,'Cooler',1500,'Fonte',1350)


print(50*'-')
print('LISTAGEM DE PREÇOS'.center(50))
print(50*'-')
a = int(len(tupla_it_var))
#print(a)
for x in range(0,a,2):
    b = int(len(tupla_it_var[x]))
    c = len(str(tupla_it_var[x+1]))
    #print(b)
    #print(c)

    print(tupla_it_var[x], (50 - b - c - 5)*'.','R$',tupla_it_var[x+1])
    #-5 pois usa 3 caracteres do R$ + do e os outros -2 não faço a mínima ideia de onde vem

print(50*'-')