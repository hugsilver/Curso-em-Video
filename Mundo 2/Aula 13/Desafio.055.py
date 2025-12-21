
vetorPeso = [0, 0, 0, 0, 0]

for i in range(0, 5, 1):
    vetorPeso[i] = float(input('Digite o peso da {}° pessoa: '.format(i+1)))

mais_pesado = max(vetorPeso)
galo = min(vetorPeso)

print('A pessoa mais pesada tem {} Kg'.format(mais_pesado))
print('A pessoa mai leve tem {} Kg'.format(galo))


#Uma opção de resolução
'''
if p == 1:
    maior = peso
    menor = peso
else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

'''



