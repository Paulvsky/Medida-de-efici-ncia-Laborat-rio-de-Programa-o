try:
    arquivo = open("relatorio_vendas.txt", "r")
except FileNotFoundError:
    print("Não foi possível achar o arquivo")
finally:
    print("Programa encerrando...")