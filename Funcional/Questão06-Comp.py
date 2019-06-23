RepeteLetra = lambda x, n: (n == 1 and x) or (RepeteLetra(x, n-1) + x)
questao = lambda x, n: map(lambda x: (x == "a" and RepeteLetra(x, n)) or (x == "e" and RepeteLetra(x, n)) or (x == "i" and RepeteLetra(x, n)) or (x == "o" and RepeteLetra(x, n)) or (x == "u" and RepeteLetra(x, n)) or x , x)



print("".join(questao(input(), int(input()))))
