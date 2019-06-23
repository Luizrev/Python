Fatorial = lambda n: (n == 1 and 1) or (n * Fatorial(n-1))
lista = lambda n: range(1, n + 1)

questao = lambda n: list(map(Fatorial, lista(n)))


print(questao(int(input("informe o numero"))))