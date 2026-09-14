numerojogador = int(input("Informe um número de 1 a 10: "))
import random
numeros = [1,2,3,4,5,6,7,8,9,10]
numeropc = random.choice(numeros)
if numerojogador == numeropc:
    print("Parabéns, vocé acertou o número sorteado pelo computador!")
else:
    print(f"Você não acertou o número sorteado pelo computador, que foi {numeropc}!")