text = 'Python крут!'

print(f'{text[0] = }')
print(f'{text[5] = }')
print(f'{text[6] = }')
print(f'{text[7] = }')
print(f'{text[-1] = }')
print(f'{text[-2] = }')
print(f'{text[-9] = }\n')

print(f'{text[4:10] = }')
print(f'{text[3:9] = }')
print(f'{text[7:-1] = }')
print(f'{text[-9:6] = }')
print(f'{text[:6] = }')
print(f'{text[6:] = }')
print(f'{text[:] = }')
print(f'{text[10:20] = }\n')

print(f'{text[1:9:2] = }')
# 1 3 5 7
print(f'{text[1:10:2] = }')
# 1 3 5 7 9
print(f'{text[8::-1] = }')
# 8 7 6 5 4 3 2 1 0
print(f'{text[:5:-1] = }')
# 11 10 9 8 7 6
print(f'{text[::-1] = }\n')
# 11 10 9 8 7 6 5 4 3 2 1 0
