from rich import print
from rich.panel import Panel


class Churrasco:
    consumo = 0.4
    precokg = 82.4
    
    def __init__(self, qtd, titulo):
        self.nome = titulo
        self.pessoas = qtd
    
    def quant_carne(self) -> float:
        return self.pessoas * Churrasco.consumo
    
    def custo_total(self) -> float:
        return self.quant_carne() * Churrasco.precokg 
    
    def custo_individual(self) -> float:
        return self.custo_total() / self.pessoas
    
    def conta(self):
        conteudo = f'Analisando o [green]{self.nome}[/] com {self.pessoas} convidados'
        conteudo += f'\nO preço para cada participante será: R${self.custo_total()}'
        conteudo += f'\nO valor para cada pessoa será R${self.custo_individual()} | (Considerando 0,400g por pessoa)'
        painel = Panel(conteudo, title=self.nome)
        print(painel)

ch = Churrasco(10, 'Churrasco da Aline')
ch.conta()