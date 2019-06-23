from functools import reduce

L = lambda: map(int, input().split())
inverte = lambda x: reduce(lambda a, x: ( map(inverte, [x]) and isinstance(x,list) or [x] ) + a  , L() , [] )

print (inverte(L))