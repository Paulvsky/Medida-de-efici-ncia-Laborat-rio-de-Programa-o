def cubo():
    global numero
    numero = float(input("Insira um número: "))
    global calcularCubo
    calcularCubo = numero ** 3
    print("O cubo do número informado é:", calcularCubo)
cubo()

def divisaoCubo():
    if numero % 3 == 0:
        calcularDivisaoCubo = calcularCubo
        print(f"{calcularDivisaoCubo}")
    else:
        calcularDivisaoCubo = False
        print(f"{calcularDivisaoCubo}")
divisaoCubo()