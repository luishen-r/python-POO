class ContaBancaria:
    """
    Cria uma conta bancária e permite realizar saques e depósitos
    """
    def __init__(self, i, t, s=0):
        self.id = i
        self.titular = t
        self.saldo = s
        print(f'Conta {self.id} criada com sucesso. Saldo: R${self.saldo:,.2f}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} autorizado')
    
    def saque(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor} na conta {self.id}. Saldo insuficiente')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} autorizado')

c1 = ContaBancaria(127077, 'Luis Henrique', 850)
c1.saque(8000)
c1.deposito(100)
print(c1) 