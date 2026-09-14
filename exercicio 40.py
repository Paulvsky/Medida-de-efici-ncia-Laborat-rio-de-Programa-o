numerojogador = int(input("Informe um número de 1 a 10: "))
import random
numeros = [1,2,3,4,5,6,7,8,9,10]
numeropc = random.choice(numeros)
if numerojogador > numeropc:
    print("O número do jogador é maior que o número sorteado pelo computador!")
else:
    print("O número do jogador é menor que o número sorteado pelo computador!!")