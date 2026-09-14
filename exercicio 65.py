numero = float(input("Insira um número: "))
calcularCubo = numero ** 3
print("O cubo do número informado é:", calcularCubo)
if numero % 3 == 0:
    calcularDivisaoCubo = calcularCubo
    print(f"{calcularDivisaoCubo}")
else:
    calcularDivisaoCubo = False
    print(f"{calcularDivisaoCubo}")