

incre = 0

n = int(input('Digite os n° primeiros números da sequência de Fibonacci que você deseja ver: '))

next = [0]*(n+2)

while (incre < n):

    next[0] = 0
    next[1] = 1
    print(next[incre], end=' -> ')
    incre += 1
    next[incre + 1] = next[incre - 0] + next[incre - 1] + next[incre + 1]

print('\nFim da sequência com {} primeiros números.'.format(n))