def validados(p):
    
    valor = p.strip().replace(',','.')

    try:
        numero = float(valor)
        if numero.is_integer():
            print('DADO VALIDO')
            return numero
        else:
            print('DADO VALIDO')
            return numero
    except ValueError:
         print('DADO NÃO VALIDO, DIGITE UM NÚMERO REAL!!!')

