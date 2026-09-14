n = int(input("Informe o valor para ser calculado o fatorial: "))
a = 1
for i in range (1,n+1):
    a *= i
    print(f"O fatorial de {n} é {a}")