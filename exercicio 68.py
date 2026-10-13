lucro = float(input("Informe o lucro: "))
n = int(input("Informe a quantidade de acionistas: "))
while True:
    try:
        divisao = lucro / n
        if n == 0:
            raise ZeroDivisionError ("A quantidade de acionistas não pode ser zero. Por favor, informe um número maior que zero")
        break 
    except ValueError:
        print("A informação inserida precisa ser número")
print(f"O valor a ser dividido é: {divisao:.2f}")