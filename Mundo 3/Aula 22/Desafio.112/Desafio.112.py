from Utilidadesdev import moeda
from Utilidadesdev import dado 


n = input('Digite o preço: R$ ')
p = dado.validados(n)
moeda.resume(p, 80, 30)

