class Termoestato:
    def __init__(self, temperatura_inicial=24):
        self.__temp = temperatura_inicial
    
    @property
    def temperatura(self):
        return self.__temp
    
    @temperatura.setter
    def temperatura(self, valor):
        if 16 <= valor <= 30 and valor == round(valor * 2) / 2:
            self.__temp = valor
            print(f'Temperatura ajustada para {valor}ºC')
        elif valor > 30:
            self.__temp = 30
        elif valor < 16:
            self.__temp = 16
        else:
            raise ValueError('Temperatura em ºC inválida')

    @property
    def ftemperatura(self):
        return f'{self.__temp:.1f}'