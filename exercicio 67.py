idade = int(input("Informe sua idade: "))
while True:
    if idade >= 0:
        print(idade)
        break
    else:
        idade = int(input("Informe sua idade novamente, de modo que seja um número maior ou igual a zero: "))