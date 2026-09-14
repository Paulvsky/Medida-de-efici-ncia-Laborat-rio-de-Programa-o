matriz = [[9,-4], [8,3]]
contador = 0
a = matriz [0][0]
b = matriz [1][1]
c = matriz [0][1]
d = matriz [1][0]
lista = [a,b,c,d]
for n in lista:
    if n > 0:
        contador += 1
print(contador)