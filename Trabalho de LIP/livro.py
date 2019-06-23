class Livro:
    def __init__(self, nome, valor, qtdEstoque, idLivro):
        self.__nome = nome
        self.__valor = valor
        self.__qtdEstoque = qtdEstoque
        self.__idLivro = idLivro
    
    def getNome(self):
        return str(self.__nome)

    def setNome(self, nome):
        self.__nome = nome

    def getValor(self):
        return int(self.__valor)

    def setValor(self, valor):
        self.__valor = valor
    
    def getQtdEstoque(self):
        return int(self.__qtdEstoque)

    def setQtdEstoque(self, qtd):
        self.__qtdEstoque = qtd

    def getId(self):
        return int(self.__idLivro)

    def setId(self, idL):
        self.__idLivro = idL

class Drama(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, capaDura):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self.__capaDura = capaDura

    def getCapa(self):
        return str(self.__capaDura)

    def toString(self):
        return "Nome: " + self.getNome() + " Valor: " + str(self.getValor()) + " Quantidade " + str(self.getQtdEstoque()) + " ID: " + str(self.getId()) + " Capa dura: " + self.getCapa

class Aventura(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, ilustracoes):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self.__ilustracoes = ilustracoes

    def getIlustracoes(self):
        return str(self.__ilustracoes)

    def toString(self):
        return "Nome: " + self.getNome() + " Valor: " + str(self.getValor()) + " Quantidade " + str(self.getQtdEstoque()) + " ID: " + str(self.getId()) + " Ilustracoes: " + self.getIlustracoes

class Comedia(Livro):
    def __init__(self, nome, valor, qtdEstoque, idLivro, brochura):
        Livro.__init__(self, nome, valor, qtdEstoque, idLivro)
        self.__brochura = brochura

    def getBrochura(self):
        return str(self.__brochura)

    def toString(self):
        return "Nome: " + self.getNome() + " Valor: " + str(self.getValor()) + " Quantidade " + str(self.getQtdEstoque()) + " ID: " + str(self.getId()) + " Brochura: " + self.getBrochura()
