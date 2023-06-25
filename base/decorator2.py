def parametrized_decorator(parameter) -> 'callable':
    """Параметризованный декоратор."""
    
    def decorator(func_obj: 'callable') -> 'callable':
        """Декоратор."""
        print(parameter)
        
        def wrapper(*args, **kwargs):
            """Обёртка."""
            print(parameter)
            return func_obj
        
        return wrapper
    
    return decorator


@parametrized_decorator('параметр')
def test_func():
    print('декорируемая функция')

# test_func = parametrized_decorator('параметр')(test_func)

test_func()
