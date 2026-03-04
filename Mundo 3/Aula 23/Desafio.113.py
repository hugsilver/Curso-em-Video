
def leiaInt():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
            return a
        except (KeyboardInterrupt, ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro valido.\033[m')

def leiaFloat():
    while True:
        try:
            b = float(input('Digite um número real: '))
            return b
        except (KeyboardInterrupt, ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real valido.\033[m')

j = leiaInt()
f = leiaFloat()

print(f'Você acabou de digitar os números - Inteiro: {j} e o Real: {f}')