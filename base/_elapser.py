from time import perf_counter_ns


def elapser(func_obj: 'callable') -> 'callable':
    """Измеряет время выполнения функции и выводит результат в stdout."""
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func_obj(*args, **kwargs)
        end = perf_counter_ns()
        print(f'Время выполнения {func_obj.__name__}() {end-start} нс')
        return result
    return wrapper


@elapser
def factorial(number: int) -> int:
    for n in range(2, number):
        number *= n
    return number


@elapser
def transform_to_set(N: int = 1000):
    return set([1]*N)

