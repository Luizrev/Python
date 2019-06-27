from livro import Livro
from livro import Drama
from livro import Aventura
from livro import Comedia

class Loja:
    def __init__(self):
        self.livros = []

    def verificaExiste(self, Id):
        tamLista = len(self.livros)

        for i in range(0, tamLista):
            if(self.livros[i]._idLivro == Id):
                return True

        return False
    
    def addLivros(self, livro):
        if(self.verificaExiste(livro._idLivro) == True):
            tamLista = len(self.livros)

            for i in range(0, tamLista):
                if(self.livros[i]._idLivro == livro._idLivro):
                    self.livros[i]._qtdEstoque += livro._qtdEstoque
        else:
            self.livros.append(livro)

    def venderLivro(self, Id, qtd = 1):
        if(self.verificaExiste(Id) == True):
            tamLista = len(self.livros)

            for i in range(0, tamLista):
                if(self.livros[i]._idLivro == Id and (self.livros[i]._qtdEstoque - qtd) >= 0 ):
                    self.livros[i]._qtdEstoque -= qtd
                    return
            print("Essa quantidade não está disponivel no estoque")
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
