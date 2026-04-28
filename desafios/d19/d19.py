from rich import print


class Livro:
    def __init__(self, titulo, pag):
        self.titulo = titulo
        self.pagina = pag
        self.pagina_atual = 1
        print(
            f':open_book: Você abriu o livro [red]{self.titulo}[/] de {self.pagina} páginas. Página atual: {self.pagina_atual}')

    def passar_pag(self, qtd=1):
        cont = 0
        for p in range(0, qtd, 1):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f' Pág {self.pagina_atual} :arrow_forward: ', end='')
                cont += 1
            else:
                print(f'\n:checkred_flag: Você chegou ao fim do livro!')
                break
        print(f'Você leu {cont} páginas')

    def fim_livro(self) -> bool:
        return self.pagina_atual >= self.pagina


l1 = Livro('Crime e Castigo', 240)
l1.passar_pag(240)

