from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("---Iniciando Preparo---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("---Bebida Pronta---")
    
    
    def ferver_agua(self):
        print(f'1. Aquecendo a água até 100ºC.')
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando a água pressurizada pelo pó de café moído.')
    
    def servir(self):
        print('3. Servindo em xícara pequena.')

class Tea(BebidaQuente):
    def misturar(self):
        print('2. Mergulhando o sachê de ervas na água.')

    def servir(self):
        print('3. Servindo na caneca de porcelana com um limão')