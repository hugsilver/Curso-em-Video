
nota1 = float(input('Digite o valor da sua 1° nota: '))
nota2 = float(input('Digite o valor da sua 2° nota: '))

media = (nota1 + nota2)/2

if media <5:
    print('Sinto muito, esta reprovado.')
elif media >=5 and media<=6.9:
    print('Tens que fazer recuperação.')
else:
    print('Aprovado.')


