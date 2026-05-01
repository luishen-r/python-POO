from classes import *


def main():
    a1 = Aluno('Luis', 18, 'Ciência da Computação', '1 - Manhã')
    print(a1.matricula())
    p1 = Professor('Edson', 38, 'Matemática', 'Superior')
    print(p1.aula())
    
    a1.estudar()
    p1.estudar()


if __name__ == '__main__':
    main()
