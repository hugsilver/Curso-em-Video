
num = int(input('Digite um número para você saber a tabuada dele: '))

print('A taboada do número {} é:'.format(num))

for i in range(1, 11, 1):
      print(' {:.1f}X{:.1f} = {:.1f}'.format(num, i, (i*num)))





