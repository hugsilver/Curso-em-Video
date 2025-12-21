
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

frase_orig = str(input('Digite uma frase: ')) #Recebendo a frase original
frase_trabalhada = "".join(frase_orig.upper().strip().split())
frase_trabalhada_inver = frase_trabalhada[::-1] #Fazendo a frase invertida já tratada

#OBS: Pode-se utilizar o método .join(var) - Exemplo: ''.join(var)

#print(frase_orig) #Teste
#print(frase_trabalhada) #Teste
#print(frase_trabalhada_inver) #Teste

frase_orig_split = frase_trabalhada.split()
frase_trabalhada_inver_split = frase_trabalhada_inver.split()

#print(frase_orig_split)
#print(frase_trabalhada_inver_split)

#print(frase_orig_split[0][0]) #Teste para ver a 1° letra salva do vetor original
#print(frase_trabalhada_inver_split[0][0]) #Teste para ver o 1° letra salva do vetor invertido

tamanho = len(frase_trabalhada)

#print(tamanho) #Observando o tamanho da frase original
count = 0

for i in range(0 , tamanho, 1):
    if(frase_orig_split[0][i] == frase_trabalhada_inver_split[0][i]):
        count += 1
    else:
        count += 0

#print(count)

print('O inverso de {} é {}'.format(frase_trabalhada, frase_trabalhada_inver))

if(count == tamanho):
    print('A frase é um POLÍNDROMO.')
else:
    print('A frase não é um POLÍNDROMO.')

#Uma outra métodologia seria:
'''
#Trabalhar pela string
inverso = '' #Inverso vazio
for letra in range(len(frase_trabalhada) - 1, -1, -1):
    inverso += junto[letra] # A string variavel recebe as letras ao contrario
Basta fazer a comparação agora com if ente a frase_trabalhada e seu inverso

'''


#Pode-se utilizar o metodo do fatiamento
#Exemplo: inverso = junto[::-1] - Como no inicio, vai até o fim, só que vai de trás para frente


