from rich import print
from rich.table import Table

tabela = Table(title='PREÇOS')
tabela.add_column('Nome', justify='center', style='yellow')
tabela.add_column('Preço', justify='center', style='green')
tabela.add_row('Notebook', 'R$3500')
tabela.add_row('Teclado', 'R$150')
print(tabela)