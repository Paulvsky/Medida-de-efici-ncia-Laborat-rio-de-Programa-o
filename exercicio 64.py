numero1 = int(input("Informe o primeiro número entre 1 e 11: "))
numero2 = int(input("Informe o segundo número entre 1 e 11: "))
numero3 = int(input("Informe o terceiro número entre 1 e 11: "))
soma = numero1 + numero2 + numero3
if soma <= 21:
    print("A soma é: ", soma)
elif soma > 21 and numero1 == 11 or numero2 == 11 or numero3 == 11:
    soma2 = soma - 10
    print("A soma é: ", soma2)
    if soma2 > 21:
        print("-1")