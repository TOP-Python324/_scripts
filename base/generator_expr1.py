numbers_str = input('числа через пробел: ')

numbers = (int(num) for num in numbers_str.split(' '))

print(type(numbers))
print(numbers, end='\n\n')

cubes = []
for n in numbers:
    cubes += [n**3]
print(*cubes, end='\n\n')

numbers_list = list(numbers)
# объект генератор уже вычислен, второе его вычисление невозможно — поэтому список будет пустым
print(numbers_list)

