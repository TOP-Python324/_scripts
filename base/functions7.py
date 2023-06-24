def draw_objects(*objects, sep=' ', end='\n') -> str:
    return sep.join(str(obj) for obj in objects) + end


draw_objects()
# '\n'

draw_objects(12, 34)
# '12 34\n'

draw_objects([5, 6])
# '[5, 6]\n'

draw_objects('abc', 7, 'def', sep='#')
# 'abc#7#def\n'



def test_func(x, y, z):
    print(f'{x=} {y=} {z=}')


test_func(2, 4, 6)
# x=2 y=4 z=6

test_func(*['a', 'b', 'c'])
# x='a' y='b' z='c'

test_func(*range(9, 12))
# x=9 y=10 z=11

test_func(*['a', 'b', 'c', 'd'])
# ... TypeError: test_func() takes 3 positional arguments but 4 were given

