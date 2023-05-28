l1 = [1, 2, 3]
l2 = l1

print(id(l1), id(l2), sep='\n')
print(f'{l1 is l2 = }\n')

l1[0] = 100

print(l1, l2, sep='\n')
