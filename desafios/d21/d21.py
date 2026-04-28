from rich import print


class Caneta:
    cor_valida = ['azul', 'vermelha', 'verde']
    
    def __init__(self, cor='azul'):
        match cor.strip().lower():
            case 'azul':
                cor_escolhida = '[blue]'
            case 'vermelha' | 'vermelho':
                cor_escolhida = '[red]'
            case 'verde':
              cor_escolhida = '[green]'
            case _:
                raise ValueError(f'Cor inválida: {cor}. Use: {", ".join(sorted(self.cor_valida))}')
        self.cor = cor_escolhida
        self.tampada = True
        
    def escrever(self, msg):
        if self.tampada:
            print(':prohibited: Não é possível escrever')
        else:
            print(f'{self.cor}{msg}[/]')
    
    def fechada(self):
        self.tampada = True
    
    def abrir(self):
        self.tampada = False

c1 = Caneta('Verde')
c1.abrir()
c1.escrever('Olá, Mundo!')
c1.fechada()
c1.escrever('Oi')
c1.abrir()
c1.escrever('POO é legal, mas confuso')