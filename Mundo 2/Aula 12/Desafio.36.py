
vcasa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o valor do seu sálario:  '))
prazo = int(input('Digite o o prazo em anos inteiro de financiamento: '))

valorMensal = vcasa/prazo

print('Sua prestação será de aproximadamente: {}'.format(vcasa/prazo))

if valorMensal < (sal*0.30):
    print('Financiamento Pré-Aprovado.')
else:
    print('Financiamento Negado.')
