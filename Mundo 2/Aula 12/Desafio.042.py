
a = int(input('Digite o 1° valor: '))
b = int(input('Digite o 2° valor: '))
c = int(input('Digite o 3° valor: '))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print('Sim, os valores podem formar um triângulo')
else:
    print('Valores não podem formar um triângulo.')

if (a == b) and (b == c) and (a == c):
    print('Triângulo equilátero pode ser formado.')
elif a == b or a == c or b == c:
    print('Triângulo Isósceles pode ser formado.')
else:
    print('Triângulo escaleno pode ser formado.')