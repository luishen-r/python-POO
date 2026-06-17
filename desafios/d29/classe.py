class Diario:
    def __init__(self, permitido=False, senha='!@#$'):
        self.permitido = permitido
        self.__senha = senha
        self.__segredos = []
    
    def acessar(self, code):
        if code == self.__senha:
            self.permitido = True
        else:
            print('Acesso negado.')
        
    def ler(self):
        if self.permitido:
            for linha in self.__segredos:
                print(f'{linha:>40}')
        else:
            print('Você não está autorizado a ler esse diário.')
    
    def escrever(self, msg):
        if self.permitido:
            palavra = str(msg)
            self.__segredos.append(palavra)
        else:
            print('Você não está permitido a escrever nesse diário')