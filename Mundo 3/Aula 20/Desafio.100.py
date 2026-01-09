from random import randint
num = list()

def lot():
    for i in range(0, 5):
        num.append(randint(0,10))
    

def sum():
    soma = 0 
    for x in num:
        if x%2 == 0:
            soma += x 
    print(soma)
     
lot()
print(num)   
sum()
