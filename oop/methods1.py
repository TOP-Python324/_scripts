from random import choice, randrange as rr
from typing import Self


class Cat:
    names: list[str] = ['Мурка', 'Черныш', 'Беляш', 'Рыжик', 'Черепаха', 'Пятно', 'Кошка']
    colors: list[str] = ['чёрный', 'белый', 'рыжий', 'черепаховый', 'серый', 'пятнистый']
    hunt_efficiency: float = 0.7
    
    def __init__(self, name: str = None, color: str = None):
        if not name:
            name = choice(self.names)
        self.name = name
        if not color:
            color = choice(self.colors)
        self.color = color
    
    @staticmethod
    def meow() -> str:
        return 'мяу'
    
    def hungry(self) -> str:
        return f"{self.name}: {'-'.join(self.meow() for _ in range(rr(2, 6)))}"
    
    def hunt(self) -> bool:
        coeff = round(self.hunt_efficiency * 10)
        hunts = [True] * coeff + [False] * (10 - coeff)
        return choice(hunts)
    
    @classmethod
    def reproduce(cls) -> list[Self]:
        return [cls() for _ in range(rr(2, 7))]
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}, {self.color}>'
    
    def __str__(self):
        return f'{self.name}: {self.color}'


# >>> yara = Cat('Яра', 'серый в полоску')
# >>> yara.name
# 'Яра'
# >>> yara.color
# 'серый в полоску'

# >>> sam = Cat('Сэм')
# >>> sam.name
# 'Сэм'
# >>> sam.color
# 'пятнистый'

# >>> Cat.meow
# <function Cat.meow at 0x000001E274FE9EE0>
# >>> yara.meow
# <function Cat.meow at 0x000001E274FE9EE0>
# >>>
# >>> Cat.meow()
# 'мяу'
# >>> yara.meow()
# 'мяу'

# >>> Cat.hungry
# <function Cat.hungry at 0x000001E274FE9F80>
# >>>
# >>> yara.hungry
# <bound method Cat.hungry of <__main__.Cat object at 0x000001E2750265D0>>
# >>>
# >>> Cat.hungry()
# ...
# TypeError: Cat.hungry() missing 1 required positional argument: 'self'
# >>>
# >>> Cat.hungry(yara)
# 'Яра: мяу-мяу-мяу-мяу'
# >>>
# >>> yara.hungry()
# 'Яра: мяу-мяу-мяу'

# Cat.reproduce() --> Cat.reproduce(Cat)
# yara.reproduce() --> Cat.reproduce(Cat)

# Class.class_method(*args, **kwargs) --> Class.class_method(Class, *args, **kwargs)
# instance.class_method(*args, **kwargs) --> instance.__class__.class_method(instance.__class__, *args, **kwargs)

# >>> for kitten in yara.reproduce():
# ...     print(f'{kitten.name}, {kitten.color}')
# ...
# Рыжик, белый
# Черныш, чёрный
# Мурка, пятнистый
# Черепаха, серый
# Беляш, белый

# >>> yara
# <Cat: Яра, серый в полоску>
# >>>
# >>> yara.__repr__()
# '<Cat: Яра, серый в полоску>'
# >>>
# >>> yara.__str__()
# 'Яра: серый в полоску'
# >>>
# >>> print(yara)
# Яра: серый в полоску
# >>>
# >>> f'{yara!s}\n{yara!r}'
# 'Яра: серый в полоску\n<Cat: Яра, серый в полоску>'
