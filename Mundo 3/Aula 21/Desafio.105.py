
import statistics

def notas(a=0 , b=0, c=0, d=0, sit = 0):

    lista = list()
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.append(d)
    lista2 = list()
    lista2.append(max(lista))
    lista2.append(min(lista))
    lista2.append(statistics.mean(lista))
    #print(lista)

    if sit == True:
        if statistics.mean([a, b, c, d])> 6:
            lista2.append('BOA')
    return lista2 



#Programa Principal
resp = notas(8, 7, sit=True)
print(resp)




