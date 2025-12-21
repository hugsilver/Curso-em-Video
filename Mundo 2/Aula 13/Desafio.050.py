soma = 0
cont = 0
for i in range(1, 7, 1):
    num = int(input('Iteração {} - Digite um número inteiro: '.format(i)))
    if num % 2 == 0: #Número PAR
        soma=soma+num
        cont += 1
print('Você informou {} números PARES e a soma é: {}'.format(cont, soma))




