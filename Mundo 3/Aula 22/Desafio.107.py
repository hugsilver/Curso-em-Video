from Desafio107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.format(p)} é {moeda.format(moeda.metade(p))}')
print(f'O dobro de {moeda.format(p)} é {moeda.format(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.format(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.format(moeda.diminuir(p, 13))}')