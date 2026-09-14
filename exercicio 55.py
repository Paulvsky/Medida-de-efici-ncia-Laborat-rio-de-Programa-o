tupla = ("Matemática", "Portugues")
dicionariojoao = {'NotaMatemática': 10, 'NotaPortuguês': 10}
a = dicionariojoao['NotaMatemática']
b = dicionariojoao['NotaPortuguês']
dicionariopedro = {'NotaMatemática': 8, 'NotaPortuguês': 9}
c = dicionariopedro['NotaMatemática']
d = dicionariopedro['NotaPortuguês']
mediaJoao = (a + b)/2
mediaPedro = (c + d)/2
if mediaJoao >= 7:
    print("João está aprovado!")
else:
    print("João está reprovado!")
if mediaPedro >= 7:
    print("Pedro está aprovado!")
else:
    print("Pedro está reprovado!")
print(tupla)