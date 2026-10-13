def numeros():
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    numero3 = float(input("Informe o terceiro número: "))
    numero4 = float(input("Informe o quarto número: "))
    numero5 = float(input("Informe o quinto número: "))
    global lista
    lista = [numero1,numero2,numero3,numero4,numero5]
numeros()

def maiordosnumeros():
    maior = max(lista)
    print("Dentre os números informados, o maior número é o:", maior)
maiordosnumeros()

def menordosnumeros():
    menor = min(lista)
    print("Dentre os números informados, o menor número é o:", menor)
menordosnumeros()