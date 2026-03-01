def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() #Por isso, essa sacada, str(input(argumento)) - Pois não lê direto da função principal
        if  entrada.isalpha() or entrada == '':
            print(f'\033[0;31m\ERRO: \"{entrada}\" é um preço inválido!\033')
        else:
            valido = True
            return float(entrada)