prompt = 'числа через пробел: '
numbers = [int(num) for num in input(prompt).split(' ')]
# то же самое 
# numbers = list(int(num) for num in input(prompt).split(' '))

print(type(numbers))
print(numbers, end='\n\n')

numbers = []
for num in input(prompt).split(' '):
    numbers += [int(num)]

print(type(numbers))
print(numbers, end='\n\n')

