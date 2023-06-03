objects = [
    'ab',
    '13',
    'cd24',
    '5',
    'ef6'
]

objects[1] = 'z13'
print(*objects, end='\n\n')


for elem in objects:
    elem = elem.upper()
print(*objects, end='\n\n')


for i in [0, 1, 2, 3, 4]:
    objects[i] = objects[i].upper()
print(*objects, end='\n\n')


