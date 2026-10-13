class ProdutoInvalidoError(Exception):
    pass

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass


def registrar_venda(produto, preco_str, quantidade_str):
    
    produto = produto.strip()
    if not produto:
        raise ProdutoInvalidoError("O nome do produto não pode estar vazio.")

    try:
        preco = float(preco_str)
        if preco <= 0:
            raise ValorInvalidoError("O preço do produto deve ser maior que zero.")
    except ValueError:
        raise ValorInvalidoError("O preço deve ser um número válido.")

    try:
        quantidade = int(quantidade_str)
        if quantidade <= 0:
            raise QuantidadeInvalidaError("A quantidade deve ser um número inteiro maior que zero.")
    except ValueError:
        raise QuantidadeInvalidaError("A quantidade deve ser um número inteiro válido.")

    total_item = preco * quantidade
    return {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total_item
    }


def gerar_relatorio(vendas):
    
    if not vendas:
        print("\n=== RELATÓRIO DIÁRIO ===")
        print("Nenhuma venda válida foi registrada hoje.")
        return

    faturamento_total = sum(venda["total"] for venda in vendas)
    total_vendas = len(vendas)
    ticket_medio = faturamento_total / total_vendas

    contagem_produtos = {}
    for venda in vendas:
        prod = venda["produto"]
        qtd = venda["quantidade"]
        contagem_produtos[prod] = contagem_produtos.get(prod, 0) + qtd
    
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)

    print("\n==================================")
    print("        RELATÓRIO DIÁRIO         ")
    print("==================================")
    print(f"Quantidade total de vendas: {total_vendas}")
    print(f"Produto mais vendido:      {produto_mais_vendido} ({contagem_produtos[produto_mais_vendido]} unidades)")
    print(f"Faturamento total:         R$ {faturamento_total:.2f}")
    print(f"Ticket médio por venda:    R$ {ticket_medio:.2f}")
    print("==================================")


def main():
    vendas_dia = []
    print("--- Sistema de Registro de Vendas da Loja Virtual ---")
    print("(Digite 'fim' no nome do produto para encerrar e gerar o relatório)\n")

    while True:
        nome_produto = input("Nome do produto: ")
        
        if nome_produto.strip().lower() == 'fim':
            break

        preco_input = input("Preço unitário: ")
        quantidade_input = input("Quantidade vendida: ")

        try:
            venda_atual = registrar_venda(nome_produto, preco_input, quantidade_input)
            
        except (ProdutoInvalidoError, ValorInvalidoError, QuantidadeInvalidaError) as erro:
            print(f"[ERRO DE VALIDAÇÃO]: {erro}")
        except Exception as erro_inesperado:
            print(f"[ERRO INESPERADO]: {erro_inesperado}")
            
        else:
            vendas_dia.append(venda_atual)
            print(f"✓ Venda de '{venda_atual['produto']}' registrada com sucesso!")
            
        finally:
            print("-" * 40)

    gerar_relatorio(vendas_dia)


if __name__ == "__main__":
    main()
