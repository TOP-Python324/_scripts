numbers = []
while True:
    try:
        num = int(input(' > '))
    except ValueError:
        break
    else:
        numbers += [num]

print()

for i in range(10):
    try:
        print(numbers[i], end='')
    finally:
        print(',', end=' ')
