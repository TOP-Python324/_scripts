def test_func(**kwargs):
    print(f'{type(kwargs)}\n{kwargs}\n')


test_func()
# <class 'dict'>
# {}

test_func(a=1)
# <class 'dict'>
# {'a': 1}

test_func(abc=123, switch=True)
# <class 'dict'>
# {'abc': 123, 'switch': True}

test_func(numbers=[1, 2, 3, 4])
# <class 'dict'>
# {'numbers': [1, 2, 3, 4]}

test_func(numbers=range(10))
# <class 'dict'>
# {'numbers': range(0, 10)}

test_func(1, 2, a=1)
# ... TypeError: test_func() takes 0 positional arguments but 2 were given

arguments = {'abc': 1, 'def': 72}

test_func(**arguments)
# <class 'dict'>
# {'abc': 1, 'def': 72}

