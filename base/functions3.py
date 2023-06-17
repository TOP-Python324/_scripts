def row_draw(numbers, sep='|', out_borders=False):
    row = f' {sep} '.join(str(n) for n in numbers)
    left_border = ('', f'{sep} ')[out_borders]
    right_border = ('', f' {sep}')[out_borders]
    return f'{left_border}{row}{right_border}'


row_draw(range(5))
# '0 | 1 | 2 | 3 | 4'

row_draw(range(5), out_borders=True)
# '| 0 | 1 | 2 | 3 | 4 |'

row_draw(range(5), True)
# '0 True 1 True 2 True 3 True 4'

row_draw(out_borders=True, numbers=range(10, 100, 10), sep='#')
# '# 10 # 20 # 30 # 40 # 50 # 60 # 70 # 80 # 90 #'

# row_draw(out_borders=True, range(10, 100, 10), '#')
# ... SyntaxError: positional argument follows keyword argument

# row_draw('_', True, numbers=[1, 2, 3])
# ... TypeError: row_draw() got multiple values for argument 'numbers'


# def test_func(x=1, y):
#     pass

# ... SyntaxError: non-default argument follows default argument
