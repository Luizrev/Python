class Livro:
    def __init__(self,nome,valor,ident):
        self.nome = nome
        self.valor = valor
        self.id = ident

class Livro_aventura(Livro):
    def __init__(self,nome,valor,ident):
        Livro.__init__(self,nome,valor,ident)
        self.genero = 'aventura'
        self.desc = 'Contem ilustracoes'
        
class Livro_drama(Livro):
    def __init__(self,nome,valor,ident):
        Livro.__init__(self,nome,valor,ident)
        self.genero = 'drama'
        self.desc = 'pode possuir capa dura'

class Livro_comedia(Livro):
    def __init__(self,nome,valor,ident):
        Livro.__init__(self,nome,valor,ident)
        self.genero = 'comedia'
        self.desc = 'pode possuir capa tipo brochura'
        
livro = Livro_comedia('comedy',100,1)
print(livro.desc)

 
    


