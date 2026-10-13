def parimpar():
    a = int(input("Informe um número: "))
    b = int(input("Informe outro número: "))
    if a % 2 == 0 and b % 2 == 0:
        print(min(a,b))
    else:
        print(max(a,b))
parimpar()