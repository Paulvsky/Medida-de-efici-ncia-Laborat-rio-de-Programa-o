class SaldoInsuficienteError(Exception):
    def __init__(self, saldoAtual, valorSaque):
        self.saldoAtual = saldoAtual
        self.valorSaque = valorSaque
        self.mensagem = "Saldo insuficiente"
        super().__init__(self.mensagem)

def realizarSaque(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    
    novoSaldo = saldo - valor
    return novoSaldo

if __name__ == "__main__":
    saldoDaConta = 500.00
    
    try:
        print(f"Saldo inicial: R${saldoDaConta:.2f}")
        saldoDaConta = realizarSaque(saldoDaConta, 600.00)
        print(f"Saque realizado com sucesso! Novo saldo: R${saldoDaConta:.2f}\n")
    except SaldoInsuficienteError as e:
        print(e)
