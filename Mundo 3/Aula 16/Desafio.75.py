

a = b = c = d = 0

a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))
c = int(input('Digite o 3° valor: '))
d = int(input('Digite o 4° valor: '))

tupla_de_4 = (a , b , c , d)
print(tupla_de_4)

print(f'O valor 9 apareceu {tupla_de_4.count(9)} na tupla')
#Método count para ver quantas vezes apareceu

if 3 in tupla_de_4:
    print(f'O valor 3 apareceu na 1° vez na posição {tupla_de_4.index(3) + 1} da tupla.')
    #Método index para achar o index que apareceu a 1° vez
else:
    print('O valor 3 não foi digitado nessa tupla.')

num_pares = tuple([x for x in tupla_de_4 if x % 2 == 0])  #Pedi ajuda

if len(num_pares) > 0:
    print(f'Os valores pares da tupla são {num_pares}')
else:
    print('Não existe valores pares nessa tupla.')
