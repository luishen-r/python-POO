from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
    
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.5
    
    def __init__(self, distancia):
        super().__init__(distancia)
    
    def calc_frete(self):
        return f'R${self.distancia * self.fator}'

class Caminhao(Transporte):
    fator = 1.2
    
    def __init__(self, distancia):
        super().__init__(distancia)
    
    def calc_frete(self):
        if self.distancia < 50:
            return f'Distância miníma para frete é de 50km'
        else:
            return f'R${self.distancia * self.fator}'
    
class Drone(Transporte):
    fator = 9.5
    
    def __init__(self, distancia):
        super().__init__(distancia)
    
    def calc_frete(self):
        if self.distancia > 10:
            return f'A distância {self.distancia}km ultrapassa os 10km permitidos.'
        else:
            return f'R${self.distancia * self.fator}'