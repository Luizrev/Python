from livro import Livro
from livro import Drama
from livro import Aventura
from livro import Comedia
from loja import Loja

print("                 .' :  `.""")
print("             .-.'`.  ;   .'`.-.""")
print("    _         / : _\ ;  /_ ; \      _")
print("      ,'_ ""--.:_;"".-."";: :"".-."":_;.--"" _`,""")
print("    :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;")
print("       `:-..J '-.-'L_ `-- ' L_..-;'")
print("            ""-._ ;  .-"  "-.  : _.-""")
print("            L ' /.------.\ ' J")
print("               ""-.   ""--""   .-""")
print("               _.l""-:_JL;-"";._")
print("          .-j/'.;  ;""""  / .'\-.""")
print("        .' /:`. ""-.:     .-" ".';  `.")
print("     .-""  / ;  ""-. ""-..-"" .-""  :    ""-. ^.")
print("  .+""-.  : :      ""-._.-"      ";-.     : :  .-+.")
print("  ; \  `.; ;                    : : ""+. ;")
print("  :  ;   ; ;                    : ;  : \:")
print(" : `.""-; ;  ;                  :  ;   ,/;")
print("  ;    -: ;  :                ;  : .-'  :")
print("  :\     \  : ;             : \.-""      :")
print("   ;`.    \  ; :            ;.'_..--  / ;")
print("   :  ""-.  ""-:  ;          :/."      ".'  :")
print("     \       .-`.\        /t-""  "":-+.   :")
print("      `.  .-"    "`l    __/ /`. :  ; ; \  ;")
print("        \   .-" ".-""-.-"  ".' .'j \  /   ;/")
print("         \ / .-" "  /.     .'.' ;_:'    ;")
print("          :-""-.`./-.'     /    `._.'")
print("                \ `t  ._  /  ")


loja = Loja()

i = True

while(i == True):
    print("-----------Bem vindo a loja do Mestre Yoda-----------")
    print("Selecione a opcao desejada: ")
    print("1) Adicionar livro ")
    print("2) Vender livro ")
    print("3) Consultar estoque ")
    print("4) Sair ")
    op = int(input())

    if(op == 1):
        print("Adicionar livros")
        print("Tipos: ")
        print("1) Comedia: ")
        print("2) Aventura: ")
        print("3) Drama: ")
        tipo = int(input("Qual é o tipo do livro? "))

        print("Informe os dados sobre o livro: ")
        nome = str(input("Informe o nome: "))
        valor = float(input("Informe o valor: "))
        quantidade = int(input("Informe a quantidade: "))
        Id = int(input("Informe o id: "))

        if(tipo == 1):
            desc = str(input("Possui brochura? "))
            livro = Comedia(nome, valor, quantidade, Id, desc)
            loja.addLivros(livro)
        elif(tipo == 2):
            desc = str(input("Possui ilustrações? "))
            livro = Aventura(nome, valor, quantidade, Id, desc)
            loja.addLivros(livro)
        elif(tipo == 3):
            desc = str(input("Possui capa dura? "))
            livro = Drama(nome, valor, quantidade, Id, desc)
            loja.addLivros(livro)
        else:
            print("Opcao invalida! ")

    elif(op == 2):
        Id = int(input("Informe o id: "))
        qtd = int(input("Informe a quantidade: "))
        loja.venderLivro(Id, qtd)
    elif(op == 3):
        loja.consultarEstoque()
    elif(op == 4):
        i = False
    else:
        print("Opcao invalida!")