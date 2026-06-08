class ContaBancaria:
    """
    Cria uma conta bancária e permite realizar saques e depósitos
    """
    def __init__(self, i, t, s=0):
        self.id = i
        self._titular = t
        self.__saldo = s
        print(f'Conta {self.id} criada com sucesso. Saldo: R${self.__saldo}')
    
    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'
    
    def deposito(self, valor):
        self.__saldo += abs(valor)
        print(f'Depósito de R${valor} autorizado')
    
    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:         
            print(f'Saque NEGADO de R${valor} na conta {self.id}. _saldoficiente')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor} autorizado')

