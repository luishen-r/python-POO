# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que possui nome e idade

    Para criar uma pessoa use
    variável = Gafanhoto(nome, idade)
    """

    def __init__(self, n='', i=0):  # Método construtor
        # Atributos de instância
        self.nome = n
        self.idade = i

    # Método de instância

    def aniversário(self):
        self.idade += 1

    def __str__(self):  # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome}; idade = {self.idade}'


# Declaração de Objetos
g1 = Gafanhoto('Luis', 18)
print(g1.__doc__)  # DUNDER Attribute
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print()
g2 = Gafanhoto('Larissa', 18)
print(g2)
print(g2.__getstate__())
