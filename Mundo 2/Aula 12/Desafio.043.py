
peso = float(input('Digite seu peso: '))
alt = float(input('Digite a altura: '))

imc = peso / (alt*alt)

print(imc)

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal.')
elif imc >=25 and imc < 30:
    print('Sobre peso.')
elif imc >= 30 and imc <=40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')


