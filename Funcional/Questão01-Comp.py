L = lambda: map(int, input().split())

M = list(filter(lambda x: x % 2 == 0, L()))

print(M)