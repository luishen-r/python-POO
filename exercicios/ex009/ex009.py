class Avaliacao:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = None
    
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, valor):
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            raise ValueError("A nota deve estar entre 0 e 10")
    
    def __str__(self):
        return f'O aluno {self.nome}, na disciplina de {self.disciplina}, está com nota {self.nota}'