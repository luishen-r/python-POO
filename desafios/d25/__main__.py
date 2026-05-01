from fretes import *
from rich import print
from rich.table import Table


def main():
    distancia = 50
    
    viagem = [Moto(distancia), Caminhao(distancia), Drone(distancia)]
    
    tabela = Table('Distância', 'Tipo', 'Frete',title='Tabela de Fretes')
    
    for x in viagem:
        tabela.add_row(
            f'{x.distancia}Km',
            type(x).__name__,
            x.calc_frete()
        )
    
    print(tabela)
    

if __name__ == '__main__':
    main()