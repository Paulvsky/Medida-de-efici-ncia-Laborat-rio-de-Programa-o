lista = ["100", "200", "300"]
for item in lista:
    try:
        preco = float(item)
    except ValueError:
        print("Informação inválida")
    else:
        precoComDesconto = preco * 0.9
        print(f"O preço original é {preco:.2f} e o preço com desconto é {precoComDesconto:.2f}")