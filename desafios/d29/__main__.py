from classe import Diario

def main():
    d = Diario()
    d.acessar('!@#$')
    d.escrever('Essa é a primeira mensagem do meu diário.')
    d.ler()


if __name__ == '__main__':
    main()