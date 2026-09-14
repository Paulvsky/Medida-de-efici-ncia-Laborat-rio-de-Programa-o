lucro = int(input("Informe o lucro: "))
if lucro == str:
    print("As informações inseridas precisam ser número")
else:
    qntAcio = int((input("Informe a quantidade de acionistas: ")))
    if qntAcio == 0 and qntAcio == str:
        print("A quantidade de acionistas não pode ser 0 e as informações inseridas precisam ser número")
    else:
        lucroDividido = float(lucro / qntAcio)
        print(lucroDividido)

#Tentei fazer da seguinte forma, mas não consegui
#while True:
    #lucro = input("Informe o lucro: ")
    #try:
        #digitado = int(lucro)
        #break
    #except ValueError:
        #print("A informação inserida precisa ser número")
    #try:

#int(digitado)
#while True:
    #n = input("Informe a quantidade de acionistas: ")
    #try:
        #digitado2 = int(n)
    #except ValueError and digitado2 != 0:
        #print("A informação inserida precisa ser número e diferente de 0")