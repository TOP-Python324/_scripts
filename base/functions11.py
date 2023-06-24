def test_func():
    """документация"""
    print('вывод функции test_func')


# работа с объектом функции
print(test_func)
print(test_func.__name__)
print(test_func.__doc__, end='\n\n')


def high_func(func_obj: 'function'):
    """функция высшего порядка"""
    print(f'{id(func_obj) = }')
    print(f'перед вызовом {func_obj.__name__}')
    func_obj()
    print(f'после вызова {func_obj.__name__}')


print(f'{id(test_func) = }')
high_func(test_func)
