soma = 0
valor = float(input("Informe o valor da nota ou 0 para parar: "))
while valor != 0:
    soma += valor
    valor = float(input("Informe o valor da nota ou 0 para parar: "))
print(f"O somatório é: {soma}")