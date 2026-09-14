lista = []

while True:
    elemento = input("Digite as notas ou digite 'sair' para parar: ")
    if elemento.lower() == 'sair':
        break
    lista.append(elemento)

print(max(lista))