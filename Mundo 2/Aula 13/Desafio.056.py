

#Essa matriz vai comportar o vetor da seguinte forma - Nome, idade e peso de 4 pessoas
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

dmenor = 0 # COntador para muqueres menores de 20 anos

for i in range(0, 4, 1):
        matrix[i][0] = str(input('Digite o nome da {} pessoa: '.format(i+1)))
        matrix[i][1] = int(input('Digite a idade da {} pessoa: '.format(i+1)))
        matrix[i][2] = str(input('Digite o sexo da {} pessoa - M para Masculino e F para Femino: '.format(i+1)))
        #print(matrix[i][1])
        if(matrix[i][1]<20 and matrix[i][2] == "F"):
            dmenor += 1 # Só assim para adicionar


soma = sum(matrix[i][1] for i in range(0, 4, 1))
#print(soma)

med = soma/4

print('A média de idade do grupo é : {}'.format(med))

if(matrix[0][2] or matrix [1][2] or matrix [2][2] or matrix[3][2] ==  "M"):
    mais_velho = max(matrix[0][1], matrix[1][1], matrix[2][1], matrix[3][1])
    if(matrix[0][1] == mais_velho) :
        print('O {} é o homem mais velho do grupo! Com {} anos.'.format(matrix[0][1]), mais_velho)
    elif(matrix[1][1] == mais_velho):
        print('O {} é o homem mais velho do grupo! Com {} anos.'.format(matrix[1][1]), mais_velho)
    elif(matrix[2][1] == mais_velho):
        print('O {} é o homem mais velho do grupo! Com {} anos.'.format(matrix[2][1]), mais_velho)
    elif(matrix[3][1] == mais_velho):
        print('O {} é o homem mais velho do grupo! Com {} anos.'.format(matrix[3][1]), mais_velho)
else:
    print('Não existem homens na lista.')


print('Existem {} mulheres com menos de 20 anos'.format(dmenor))







