class Livro:
    def __init__(self, nome, valor, qtdEstoque, idLivro):
        self._nome = nome
        self._valor = valor
        self._qtdEstoque = qtdEstoque
        self._idLivro = idLivro

class Drama(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, capaDura):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self._capaDura = capaDura

    def toString(self):
        return "Nome: " + self._nome + " Valor: " + str(self._valor) + " Quantidade " + str(self._qtdEstoque) + " ID: " + str(self._idLivro) + " Capa dura: " + self._capaDura

class Aventura(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, ilustracoes):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self._ilustracoes = ilustracoes

    def toString(self):
        return "Nome: " + self._nome + " Valor: " + str(self._valor) + " Quantidade " + str(self._qtdEstoque) + " ID: " + str(self._idLivro) + " Ilustracoes: " + self._ilustracoes

class Comedia(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, brochura):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self._brochura = brochura

    def toString(self):
        return "Nome: " + self._nome + " Valor: " + str(self._valor) + " Quantidade " + str(self._qtdEstoque) + " ID: " + str(self._idLivro) + " Brochura: " + self._brochura
