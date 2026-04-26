#Declaração de Classe
class Gafanhoto:
    def __init__(self): #Método construtor
        #Atributos de instância
        self.nome = ''
        self.idade = 0
    
    
    #Método de instância
    def aniversário(self):
        self.idade += 1
    
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

 
#Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Luis'
g1.idade = 18
g1.aniversário()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Larissa'
g2.idade = 18
print(g2.mensagem())
   