L = [1,2,3,4,5]
quickSort = lambda x : x and quickSort([0])+[x[0]] + quickSort([x[1:] and i > x[0]])
print(quickSort(L))