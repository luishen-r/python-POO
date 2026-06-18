class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = None
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if valor > 0:
            self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
    
    @property
    def area(self):
        return self._base * self._altura
    
    @area.setter
    def area(self):
        self._area = self._base * self._altura
    
    @property
    def medidas(self):
        return f'Base = {self._base} | Altura = {self._altura}'
    
    @medidas.setter
    def medidas(self, valores):
        self._base, self._altura = valores