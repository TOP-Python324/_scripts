from collections.abc import Callable
from functools import cache
from time import perf_counter_ns as pc_ns


def elapse(func_obj: Callable) -> Callable:
    # print(func_obj)
    def __wrapper(self, *args, **kwargs):
        start = pc_ns()
        res = func_obj(self, *args, **kwargs)
        end = pc_ns()
        print(f'elapsed time for {func_obj.__name__}(): {end-start} ns')
        return res
    return __wrapper


class Person:
    _default_format: str = 'name_patr'
    
    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    def __hash__(self):
        return hash(f'{self.last_name}{self.first_name}{self.patr_name}')
    
    @property
    @cache
    def _full(self) -> str:
        print('вызов _full')
        return f'{self.last_name} {self.first_name} {self.patr_name}'
    
    @property
    @cache
    def _initials_start(self) -> str:
        print('вызов _initials_start')
        return f'{self.first_name[0]}. {self.patr_name[0]}. {self.last_name}'
    
    @property
    @cache
    def _initials_end(self) -> str:
        print('вызов _initials_end')
        return f'{self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'
    
    @property
    @cache
    def _name_patr(self) -> str:
        print('вызов _name_patr')
        return f'{self.first_name} {self.patr_name}'
    
    @elapse
    def __repr__(self):
        return getattr(self, f'_{self._default_format}')


silva = Person('Градская', 'Сильва', 'Арсениевна')

# >>> silva
# Сильва Арсениевна
# >>>
# >>> Person._default_format = 'full'
# >>> silva
# Градская Сильва Арсениевна
# >>>
# >>> Person._default_format = 'initials_start'
# >>> silva
# С. А. Градская
# >>>
# >>> Person._default_format = 'initials_end'
# >>> silva
# Градская С. А.


# >>> hash(silva)
# 4748813286768979806
# >>>
# >>> silva
# elapsed time for __repr__(): 12300 ns
# Сильва Арсениевна
# >>>
# >>> silva.first_name = 'Алёна'
# >>>
# >>> hash(silva)
# 8486893417668426607
# >>>
# >>> silva
# elapsed time for __repr__(): 16500 ns
# Алёна Арсениевна
