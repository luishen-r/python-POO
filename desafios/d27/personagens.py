from abc import ABC, abstractmethod
from random import choice, randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes
    
    def atacar(self, alvo, forca):
        dano = round(forca * randint(1, 20) / 20, 2)
        golpe = choice(self.golpes)
        print(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] com {dano} de dano')
        alvo.receber_dano(dano)
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f'{self.nome} foi derrotado!')
        else:
            print(f'{self.nome} agora tem {self.vida} pontos de vida')
        
    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
    
    def curar(self):
        cura = 15
        self.vida += cura
        print(f'O Guerreiro {self.nome} curou {cura} pontos de vida!')
    
class Mago(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
    
    def curar(self):
        cura = 25
        self.vida += cura
        print(f"O Mago {self.nome} usou magia de luz e recuperou {cura} de vida!")
        