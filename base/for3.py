fruits = []
while True:
    fruit = input('фрукт: ')
    if not fruit:
        break
    # fruits = fruits + [fruit]
    fruits += [fruit]
print()


number_of_fruits = len(fruits)
for i in range(number_of_fruits):
    print(f'{i=} {fruits[i]}')
print()


for i in range(number_of_fruits):
    fruits[i] = fruits[i][::-1]

print(*fruits, sep='\n', end='\n\n')


for i, fruit in enumerate(fruits):
    fruits[i] = fruit[::-1]

print(*fruits, sep='\n', end='\n\n')

