from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5
    
    def __init__(self, canal=1, volume=2):
        self.canal = canal
        self.volume = volume
        self.ligar:bool = False
    
    def botao_ligar(self):
        self.ligar = not self.ligar
    
    def mostrar_tv(self):
        if  not self.ligar:
          tv = Panel(f':Prohibited: [red]A TV está desligada[/]', title='TV', width=40)
        else:
            conteudo = f'CANAL = '
            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if c == self.canal:
                    conteudo += f' [white on yellow]{c}[/] '
                else:
                    conteudo += f' {c} '
            conteudo += f'\nVOLUME = '
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'
            tv = Panel(conteudo, title='[ TV ]', width=30)
        print(tv)
        
    def canal_mais(self):
        if self.ligar:
            if ControleRemoto.canal_max == self.canal:
                self.canal = ControleRemoto.canal_min
            else:
                self.canal += 1
           
                
    def canal_menos(self):
        if self.ligar:
            if ControleRemoto.canal_min == self.canal:
                    self.canal = ControleRemoto.canal_max
            else:
                self.canal -= 1
        
    def volume_mais(self):
        if self.ligar:
            if self.volume != ControleRemoto.volume_max:
                self.volume += 1
            else:
                pass
    
    def volume_menos(self):
        if self.ligar:
            if self.volume != ControleRemoto.volume_min:
                self.volume -= 1
            else:
                pass

televisão = ControleRemoto()
while True:
    televisão.mostrar_tv()
    comando = str(input(f'\n < CH{televisão.canal} >  - VOL{televisão.volume} +  '))
    match comando:
        case '0':
            break
        case '@':
            televisão.botao_ligar()
        case '<':
            televisão.canal_menos()
        case '>':
            televisão.canal_mais()
        case '-':
            televisão.volume_menos()
        case '+':
            televisão.volume_mais()
        case _:
            raise ValueError (f'O comando {comando} não existe.')