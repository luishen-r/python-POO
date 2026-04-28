from rich import print
from rich.panel import Panel


class Etiqueta:
    def __init__(self, produto, preco):
        self.nome = produto
        self.valor = preco
    
    def __str__(self):
        return f'{self.nome} custa R${self.valor:,.2f}'

    def ficha(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self.valor:,.2f}'
        conteudo += f'{precof.center(30, '.')}'
        etiqueta = Panel(conteudo,title='Produto', width=34)
        print(etiqueta)
         
p1 = Etiqueta('Camisa', 350)
print(p1)
p1.ficha()
p2 = Etiqueta('Notebook', 3500)
p2.ficha()
        