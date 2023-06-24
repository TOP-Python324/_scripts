print('вводите координаты точек по порядку их соединения в многоугольник')
prompt = 'X Y: '

coords = [
    [int(c) for c in input(prompt).split()],
    [int(c) for c in input(prompt).split()],
    [int(c) for c in input(prompt).split()]
]
while (inp := input(prompt)):
    coords += [[int(c) for c in inp.split()]]


# переменная для аннотации
Point = tuple[int, int]


def polygon_perimeter(
        point1: Point, 
        point2: Point, 
        point3: Point, 
        *points: Point
) -> float:
    """Вычисляет периметр многоугольника, построенного из последовательности точек."""
    # объединение обязательных и необязательных аргументов
    print(point1, point2, point3, points)
    
    points = (point1, point2, point3) + points
    
    perimeter = 0
    for i in range(-1, len(points)-1):
        # print(f'{i=}\t{i+1=}')
        # print(f'{points[i]}\t{points[i+1]}')
        
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        
        perimeter += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    return perimeter


# X Y: 0 0
# X Y: 5 0
# X Y: 5 5
# X Y: 0 5
# X Y:
# >>> polygon_perimeter(*coords)
# [0, 0] [5, 0] [5, 5] ([0, 5],)
# 20.0
