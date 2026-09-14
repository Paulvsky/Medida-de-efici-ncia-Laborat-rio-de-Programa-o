temp1 = float(input("Informe a primeira temperatura: "))
temp2 = float(input("Informe a segunda temperatura: "))
temp3 = float(input("Informe a terceira temperatura: "))
temp4 = float(input("Informe a quarta temperatura: "))
temp5 = float(input("Informe a quinta temperatura: "))
lista = [temp1,temp2,temp3,temp4]
media = float((temp1+temp2+temp3+temp4+temp5)/5)
if 18 < media < 28:
    print("A média está dentro da faixa ideal de cultivo")
else:
    print("A média não está dentro da faixa ideal de cultivo")
print(lista)