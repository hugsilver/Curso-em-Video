#Não consgeui

num = int(input('Digite um valor para achar seu fatorial: '))

fat = 0
n = num

while (n > 1):
    n1 = num*(n-1)
    fat = num
    fat = (fat)*n1
    print(n1)
    print(fat)
    n -= 1

print('O fatorial de {} é {}'.format(num , fat))