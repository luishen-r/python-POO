from personagens import *


def main():
    g1 = Guerreiro('Ramon', 3000, ['Empurrada', 'Socão'])
    m1 = Mago('Filho', 2500, ['Bola de Fogo', 'Cristalização'])
    
    g1.atacar(m1, 1000)
    m1.atacar(g1, 1000)
    g1.curar()


if __name__ == '__main__':
    main()