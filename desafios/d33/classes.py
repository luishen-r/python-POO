from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome, ano_nascimento=None):
        self._nome = nome
        
        if ano_nascimento == None:
            ano = int(input('Informe seu ano de nascimento: '))
            self.nascimento = ano
        else:
            self.nascimento = ano_nascimento
        
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, ano):
        if date.today().year - 120 <= ano <= date.today().year:
            self._nascimento = ano
            return
        else:
            raise ValueError(f'Ano {ano} é inválido.')
    
    @property
    def idade(self):
        return date.today().year - self._nascimento
    
    @idade.setter
    def idade(self, valor):
        raise PermissionError('Não é possível alterar diretamente a idade do aluno.')
    
class Aluno(Pessoa):
    cursos = ['ADM', 'ADS', 'ENG']
    
    def __init__(self, nome, ano_nascimento=None, curso=None):
        super().__init__(nome, ano_nascimento)
        
        if curso is None:
            curso = str(input('Informe o seu curso: '))
        self.curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, nome):
        if nome not in self.cursos:
            raise ValueError(f'O curso {nome} não está disponível.')
        self._curso = nome
    
    @classmethod
    def add_curso(cls, curso):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            if curso not in cls.cursos:
                cls.cursos.append(curso)
                print(f'Curso {curso} foi adicionado a lista de cursos.')
            else:
                print(f'"{curso}" já está presente na lista de cursos.')
        else:
            print(f'Curso {curso} não está na formatação de siglas. Por favor insira as siglas do curso com no máximo 5 caracteres.')
        