from collections.abc import Iterable
from numbers import Number


class OrderedNumbers(list):
    def __init__(self, numbers: Iterable[Number]):
        for n in numbers:
            if not isinstance(n, Number):
                raise ValueError
        super().__init__(sorted(numbers))
    
    def __setitem__(self, index: int, value: Number):
        if not isinstance(value, Number):
            raise ValueError
        super().__setitem__(index, value)
        self.sort()
    
    def append(self, value: Number):
        if not isinstance(value, Number):
            raise ValueError
        super().append(value)
        self.sort()
    
    def extend(self, numbers: Iterable[Number]):
        for n in numbers:
            if not isinstance(n, Number):
                raise ValueError
        super().extend(numbers)
        self.sort()
    
    def insert(self, index_, value: Number):
        self.append(value)

