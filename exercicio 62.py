numero = int(input("Insira um número: "))
soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i
        if soma == numero:
            print(f"O número {numero} é perfeito")
        else:
            print(f"O número {numero} não é perfeito")