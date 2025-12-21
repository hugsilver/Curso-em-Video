
num = c = 0

while True:
    num = int(input('Digite um numero para ver sua taboada - OBS: Digite um número negativo para sair: '))
    c = 0
    if num > 0:
        for c in range(1,10):
            print(num,'X',c, '=', c*num)
            c += 1
    if num < 0:
        break


