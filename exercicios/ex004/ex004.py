#Herança é um relacionamento entre itens gerais(ancestrais) e tipos mais específicos(descendentes) desses itens, que herdam atributos e metódos dos niveis superiores
#Vantagens: Reutilazação de código; Organização hierárquica
from rich import inspect, print

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversário(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def matricula(self):
        return f'{self.nome} acabou de se matricular'

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

a1 = Aluno('Luis', 18, 'Ciência da Computação', '1 - Manhã')
print(a1.matricula())
p1 = Professor('Edson', 38, 'Matemática', 'Superior')
inspect(a1)
inspect(p1)