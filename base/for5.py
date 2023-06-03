objects = [
    'ab',
    '13',
    'cd24',
    '5',
    'ef6'
]


counter = 0
for elem in objects:
    for char in elem:
        if char in '0123456789':
            counter += 1
print(counter, end='\n\n')



for i in range(5):
    print(f'{i = }', end='')
    for j in range(4):
        # if j == 2:
            # print('_'*9, end='')
        print(f'\t{j = }')
    print(f'конец {i+1}-ой итерации внешнего цикла')

