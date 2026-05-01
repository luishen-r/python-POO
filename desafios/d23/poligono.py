from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd):
        self.lados:int = qtd
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, qtd):
        super().__init__(4)
        self.lado = qtd
        
    
    def perimetro(self):
        return self.lado*4

    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, qtd):
        super().__init__(qtd)
        self.raio = qtd
    
    def perimetro(self):
        return self.raio*2*3
    
    def area(self):
        return 3*(self.raio**2)

        