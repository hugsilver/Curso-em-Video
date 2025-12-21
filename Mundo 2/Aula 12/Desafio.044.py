
valor = float(input('Digite o valor do produto: R$ '))

print('1 - Pagamento a vista no dinheiro. \n2 - A vista no cartão. \n3 - Até 2 vezes no cartão. \n4 - 3 vezes ou mais no cartão.\n')

op = int(input('Digite a opção desejada: '))

if op == 1:
    print('A vista no dinehiro fica : {}'.format(valor*0.9))
elif op == 2:
    print('A vista no cartão fica : {}'.format(valor*0.95))
elif op == 3:
    print('Em duas vezes no cartão fica : {}'.format(valor))
elif op == 4:
    print('Em 3 vezes ou mais no cartão fica: {}'.format(valor*1.20))
else:
    print('Opção invalida.')


