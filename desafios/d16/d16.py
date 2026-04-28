from rich import print


class Funcionario:
    # Atributos de Classe
    Empresa = 'Bradesco'

    def __init__(self, n, s, c):
        self.nome = n
        self.setor = s
        self.cargo = c

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/], trabalho no setor {self.setor} e meu cargo é {self.cargo}, na empresa {Funcionario.Empresa}'


c1 = Funcionario('Luis', 'Equipe de Devs', 'Analista de Dados')
apr = c1.apresentacao()
print(apr)
