
cont = soma = n = 0

while True:
    n = int(input('Digite um valor - OBS: 999 para parar: '))
    if n != 999:
        soma += n
        cont += 1
    if n == 999:
        break

print(f'A soma dos {cont} números é {soma}.')







