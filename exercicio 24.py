lista = []

while True:
    nome = input("Registre os nomes dos participantes ou 'sair' para parar: ")
    if nome.lower() == 'sair':
        break
    lista.append(nome)
lista.reverse()
print(lista)