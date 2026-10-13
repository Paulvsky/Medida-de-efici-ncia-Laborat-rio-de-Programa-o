class ValorInvalidoError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    pass

def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValorInvalidoError("O valor a sacar deve ser maior que zero")
    if valor_saque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")
    novoSaldo = saldo - valor_saque
    return novoSaldo

if __name__ == "__main__":
    saldo_atual = 500.00
    print(f"Saldo atual: R$ {saldo_atual:.2f}\n")
    
    valor_pretendido = 150.00 
    
    try:
        
        novo_saldo = realizar_saque(saldo_atual, valor_pretendido)
        print(f"Saque de R$ {valor_pretendido:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {novo_saldo:.2f}")
        
    except ValorInvalidoError as e:
        print(f"Erro de Operação: {e}")
        
    except SaldoInsuficienteError as e:
        print(f"Erro de Saldo: {e}")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")