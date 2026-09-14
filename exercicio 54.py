matriz = [[1,0,1], [1,1,0], [0,1,1]]
contador1 = 0
contador2 = 0
#lista = [1,0,1,1,1,0,0,1,1]
#a,b,c,d,e,f,g,h,i = lista
a = matriz [0][0]
b = matriz [0][1]
c = matriz [0][2]
d = matriz [1][0]
e = matriz [1][1]
f = matriz [1][2]
g = matriz [2][0]
h = matriz [2][1]
i = matriz [2][2]
lista = [a,b,c,d,e,f,g,h,i]
for n in lista:
    if n == 0:
        contador1 += 1
for m in lista:
    if m == 1:
        contador2 += 1
print(f"A quantidade de vagas ocupadas é {contador2}")
print(f"A quantidade de vagas livres é {contador1}")