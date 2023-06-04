print('вводите координаты точек по порядку их соединения в многоугольник')
prompt = 'X Y: '

coords = [
    [int(c) for c in input(prompt).split()],
    [int(c) for c in input(prompt).split()],
    [int(c) for c in input(prompt).split()]
]

while (inp := input(prompt)):
    coords += [[int(c) for c in inp.split()]]

# print(coords)

perimeter = 0

for i in range(-1, len(coords)-1):
    # print(f'{i=}\t{i+1=}')
    # print(f'{coords[i]}\t{coords[i+1]}')
    
    x1, y1 = coords[i]
    x2, y2 = coords[i+1]
    
    perimeter += ((x1 - x2)**2 + (y1 - y2)**2)**0.5

