a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
if a % 2 == 0 and b % 2 == 0 and a < b:
    print(a)
elif a % 2 == 0 and b % 2 == 0 and b < a:
    print(b)
elif a % 2 != 0 or b % 2 != 0 and a < b:
    print(b)
elif a % 2 != 0 or b % 2 != 0 and b < a:
    print(a)