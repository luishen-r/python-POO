from abc import ABC, abstractmethod
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.salario = None
        self.sal_bruto = None
        self.sal_minimo = 1612
        self.inss = 0.075
    
    @abstractmethod
    def calc_sal(self):
        pass
    
    def analisar_sal(self):
        return Panel(f'O funcionário [blue]{self.nome}[/] recebe um salário de [green]R${self.salario:,.2f}[/]. O que corresponde a {self.salario/self.sal_minimo:,.2f} salários minimos.', title='Analise de Salário', width=45)
    
class Horista(Funcionario):
    def __init__(self, nome, vhora, horas):
        super().__init__(nome)
        self.valor_hora = vhora
        self.horas_trab = horas
    
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto*self.inss)
        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome, bruto=1612):
        super().__init__(nome)
        self.sal_bruto = bruto
        
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss)
        return self.salario
        
