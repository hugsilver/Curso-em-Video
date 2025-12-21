
soma = 0 # Acumulador
cont = 0 #Contador
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i #Não é um acumulador, mas sim somador. Pode ser usar a sintaxe +=
        cont += 1 # Contador conta mais um - Soma mais um
print('A soma dos {} valores impares que são multiplos de 3 entre 1 e 500 é {}'.format(cont, soma))