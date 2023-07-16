from functools import wraps


def decorator(func_obj: 'callable') -> 'callable':
    """Декоратор"""
    print('начало вызова функции-декоратора')
    
    @wraps(func_obj)
    def wrapper(*args, **kwargs):
        """Обёртка"""
        print('\tначало вызова функции-обёртки')
        result = func_obj(*args, **kwargs)
        print('\tконец вызова функции-обёртки')
        return result
    
    print('конец вызова функции-декоратора')
    return wrapper


def test_func():
    print('\t\tвызов декорируемой функции')


print(test_func)
test_func = decorator(test_func)
print(test_func)
print(test_func(), end='\n\n')

# >>> test_func.__name__
# 'wrapper'
# >>> test_func.__doc__
# 'Обёртка'


@decorator
def adder(n1, n2):
    """Сумматор"""
    return n1 + n2
# adder = decorator(adder)


print(adder(5, 9), end='\n\n')

# >>> adder.__name__
# 'wrapper'
# >>> adder.__doc__
# 'Обёртка'
