lista = []
while True:
    produto = input("Informe um produto cadastrado no sistema ou digite 'sair' para parar: ")
    if produto.lower() == 'sair':
        break
    lista.append(produto)
print("A quantidade de elementos existentes na lista é ", len(lista))