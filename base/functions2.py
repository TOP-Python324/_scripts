def adder(number1, number2):
    print(f'{number1=} {number2=}')
    return number1 + number2


result = adder(12, 5)
print(result)

prompt = '\n введите число > '
result = adder(int(input(prompt)), int(input(prompt)))
print(result)


result = adder(number1=100, number2=25)
print(result)

result = adder(number2=25, number1=100)
print(result, end='\n\n')

# >>> adder(1)
# ... TypeError: adder() missing 1 required positional argument: 'number2'
# >>>
# >>> adder()
# ... TypeError: adder() missing 2 required positional arguments: 'number1' and 'number2'


def multiplier(x, y=1):
    print(f'{x=} {y=}')
    return x * y


multiplier(9, 6)
multiplier(15)

# >>> multiplier(y=2)
# ... TypeError: multiplier() missing 1 required positional argument: 'x'

