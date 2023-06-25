prompt = ' введите последовательность чисел > '

numbers = map(
    lambda n: int(n) if n.isdecimal() else 0, 
    input(prompt).split()
)

#  введите последовательность чисел > 1 5 6 a 8 -10 25
# >>>
# >>> list(numbers)
# [1, 5, 6, 0, 8, 0, 25]

numbers = filter(
    lambda n: n != 0,
    numbers
)

# >>> list(numbers)
# [1, 5, 6, 8, 25]

