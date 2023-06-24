def test_func(*args):
    print(f'{type(args)}\n{args}\n')


test_func()
# <class 'tuple'>
# ()

test_func(7)
# <class 'tuple'>
# (7,)

test_func(7, 8, 9)
# <class 'tuple'>
# (7, 8, 9)

test_func(10, 'abc')
# <class 'tuple'>
# (10, 'abc')

numbers = [4, 10, 2, 8, 5]

test_func(numbers)
# <class 'tuple'>
# ([4, 10, 2, 8, 5],)

test_func(numbers, numbers[::-1])
# <class 'tuple'>
# ([4, 10, 2, 8, 5], [5, 8, 2, 10, 4])

test_func(*numbers)
# <class 'tuple'>
# (4, 10, 2, 8, 5)

test_func(1, 2, *range(3, 10))
# <class 'tuple'>
# (1, 2, 3, 4, 5, 6, 7, 8, 9)

