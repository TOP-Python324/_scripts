l1 = [1, 2, 3]
print(id(l1), l1)

l1.append(4)
print(id(l1), l1)

l1.extend([5, 6])
print(id(l1), l1)

l1 = l1 + [7]
# l1 += [7]
print(id(l1), l1)

l1.clear()
print(id(l1), l1)

