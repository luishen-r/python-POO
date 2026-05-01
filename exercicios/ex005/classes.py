from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversário(self):
        self.idade += 1
    
    @abstractmethod
    def estudar():
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def matricula(self):
        return f'{self.nome} acabou de se matricular'
    
    def estudar(self):
        print(f'O aluno {self.nome} está estudando{self.curso}')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def aula(self):
        return f'O professor {self.nome} está dando aula'
    
    def estudar(self):
        print(f'O professor {self.nome} é especialista em {self.especialidade} no {self.nivel}')