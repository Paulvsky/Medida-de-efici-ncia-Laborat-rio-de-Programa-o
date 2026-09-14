lista = []

while True:
    valor = input("Digite um valor ou digite 'sair' para parar: ")
    if valor.lower() == 'sair':
        break
    try:
        numero = float(valor)
        lista.append(numero)
    except ValueError:
        print("Informe número válido ou 'sair' para parar")

soma = sum(lista)
print(soma)