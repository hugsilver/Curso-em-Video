
tupla_palavras = ('aprender', 'programar', 'linguagem', 'pyhton' , 'curso' , 'gratis' ,
                   'estudar', 'praticar' , 'trabalhar' , 'mercado', 'programador' , 'futuro' )

print(tupla_palavras)

for x in tupla_palavras:
    #print(x.upper())
    print(f'Na palavra {x.upper()} existem as vogais: ', end='')
    if 'A' in x.upper():
        print('a', end='')
    if 'E' in x.upper():
        print('e', end='')
    if 'I' in x.upper():
        print('i', end='')
    if 'O' in x.upper():
        print('o', end='')
    if 'U' in x.upper():
        print('u')
    print('\n')