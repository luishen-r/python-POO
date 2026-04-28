from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    
    def add_jogos(self, *jogo):
        self.jogos.extend(jogo)
    
    def status(self):
        conteudo = f'Nome real: {self.nome}'
        conteudo += '\nJogos mais jogados: '
        for i, j in enumerate(self.jogos):
            conteudo += f'\n:video_game: {i+1}: {j}'
        painel = Panel(conteudo, title=f'Jogador {self.nick}', width=None)
        return painel

jogador1 = Gamer('Luis', 'silentzxs_')
jogador1.add_jogos('GTA 5', 'Fortnite', 'FIFA 24', 'GTA San Andreas')
ficha = jogador1.status()
print(f'{"FICHA GAMER".center(40, '-')}') 
print(ficha)    