import hashlib
from rich import print

class Credencial:
    def __init__(self, senha_inicial: str = ''):
        self.senha = senha_inicial
    
    @property
    def senha(self):
        """Getter para a propriedade senha (por segurança, não expõe o valor real)."""
        return "Acesso restrito: Use o método validar() para testar uma senha."

    @senha.setter
    def senha(self, senha_nova: str):
        """Setter que intercepta a senha em texto limpo e armazena apenas o hash SHA-256."""
        senha_bytes = senha_nova.encode('utf-8')
        self.__hash = hashlib.sha256(senha_bytes).hexdigest()
    
    def validar(self, chave: str):
        """Método público que compara o hash da chave fornecida com o hash armazenado."""
        chave_bytes = chave.encode('utf-8')
        hash_chave = hashlib.sha256(chave_bytes).hexdigest()
        if hash_chave == self.__hash:
            print('Senha correta.')
            print('[green]True[/]')
        else:
            print('Senha inválida.')
            print('[red]False[/]')