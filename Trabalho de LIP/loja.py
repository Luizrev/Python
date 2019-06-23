from livro import Livro
from livro import Drama
from livro import Aventura
from livro import Comedia

class Loja:
    def __init__(self):
        self.livros = []

    def verificaExiste(self, idLivro):
        tamLista = len(self.livros)

        for i in range(0, tamLista):
            if(self.livros[i].getId() == idLivro):
                return True

        return False
    
    def addLivros(self, livro):
        if(self.verificaExiste(livro.getId()) == True):
            tamLista = len(self.livros)

            for i in range(0, tamLista):
                if(self.livros[i].getId() == livro.getId()):
                    self.livros[i].setQtdEstoque(self.livros[i].getQtdEstoque() + livro.getQtdEstoque())
        else:
            self.livros.append(livro)

    def venderLivro(self, idLivro, qtd = 1):
        if(self.verificaExiste(idLivro) == True):
            tamLista = len(self.livros)

            for i in range(0, tamLista):
                if(self.livros[i].getId() == idLivro and self.livros[i].getQtdEstoque() >= 1):
                    self.livros[i].setQtdEstoque(self.livros[i].getQtdEstoque() - qtd)
                    return
            print("O livro nao esta disponivel em estoque")
        else:
            print("O livro nao existe")

    def consultarEstoque(self):
        tamLista = len(self.livros)

        print("Lista de livros: ")
        for i in range(0, tamLista):
            print(self.livros[i].toString())

    def teste(self):
        if(12 in self.livros):
            print("OK")
