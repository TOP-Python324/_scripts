from time import perf_counter_ns


def elapser(func_obj: 'callable') -> 'callable':
    """Измеряет время выполнения функции и выводит результат в stdout."""
    print('декоратор elapser')
    
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func_obj(*args, **kwargs)
        end = perf_counter_ns()
        print(f'Время выполнения {func_obj.__name__}() {end-start} нс')
        return result
    
    return wrapper


def cache(func_obj: 'callable') -> 'callable':
    """Кеширует результаты вызова функции для набора аргументов."""
    print('декоратор cache')
    results = {}
    
    def wrapper(*args, **kwargs):
        key = *args, *kwargs.items()
        if key not in results:
            results[key] = func_obj(*args, **kwargs)
        return results[key]
    
    return wrapper


@elapser
@cache
def factorial(number: int) -> int:
    for n in range(2, number):
        number *= n
    return number

# истинный порядок применения декораторов
# factorial = cache(factorial)
# factorial = elapser(factorial)

