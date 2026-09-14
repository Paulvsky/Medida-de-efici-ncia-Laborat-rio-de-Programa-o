lista = ["1", "2", "3"]
codigo = input("Informe um codigo no sistema: ")
    
if codigo in lista:
    print(f"Sim, '{codigo}' está na lista!")
else:
    print(f"Não, '{codigo}' não está na lista!")