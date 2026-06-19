import sys
import hashlib

def capturar_senha(prompt='Digite a senha: '):
    """Função auxiliar para ler a entrada do teclado mostrando apenas '*'."""
    print(prompt, end='', flush=True)
    senha = ''
    
    if sys.platform == "win32":
        import msvcrt
        while True:
            ch = msvcrt.getch()
            if ch in (b'\r', b'\n'):  # Enter
                print()
                break
            elif ch == b'\x08':  # Backspace
                if len(senha) > 0:
                    senha = senha[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            else:
                try:
                    senha += ch.decode('utf-8')
                    sys.stdout.write('*')
                    sys.stdout.flush()
                except UnicodeDecodeError:
                    pass
        return senha
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                if ch in ('\r', '\n'):  # Enter
                    print()
                    break
                elif ch in ('\x7f', '\x08'):  # Backspace
                    if len(senha) > 0:
                        senha = senha[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                else:
                    senha += ch
                    sys.stdout.write('*')
                    sys.stdout.flush()
        finally:
            # Garante o retorno das configurações originais do terminal no Linux/Mac
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return senha


class ContaBancaria:
    def __init__(self, id_conta: int, titular: str, saldo_inicial: float, senha=None):
        self._id = id_conta
        self._titular = titular
        self.__saldo = saldo_inicial
        
        if senha is None:
            print(f'\n[SEGURANÇA] Criando conta de {self._titular}. Nenhuma senha foi informada.')
            senha = self.pede_senha()
        
        self.__hash = self.__gerar_hash(senha)
    
    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novo_nome):
        self._titular = novo_nome
    
    def __gerar_hash(self, senha_texto_puro):
        return hashlib.sha256(senha_texto_puro.encode('utf-8')).hexdigest()
    
    def validar_senha(self, chave):
        return self.__hash == self.__gerar_hash(chave)
    
    def pede_senha(self):
        return capturar_senha('Informe a senha da conta: ')
    
    def sacar(self, valor, chave=None):
        if chave is None:
            chave = self.pede_senha()
        
        if not self.validar_senha(chave):
            print('ERRO: Senha incorreta! Operação de saque cancelada')
            return False

        if valor <= 0:
            print('ERRO: O valor de saque deve ser positivo.')
            return False
        
        if valor > self.__saldo:
            print('ERRO: Saldo insuficiente.')
            return False
        
        self.__saldo -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        return True
    
    def depositar(self, valor):
        chave = self.pede_senha()
        
        if not self.validar_senha(chave):
            print('ERRO: Senha incorreta. Finalizando a operação.')
            return False
        
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito no valor de R${valor:.2f} realizado com sucesso.')
            return True
        else:
            print('ERRO: O valor do depósito deve ser positivo.')            
            return False
        
    def exibir_saldo(self):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            print(f'Saldo Atual: R${self.__saldo:.2f}')
        else:
            print('ERRO: Senha inválida.')
        