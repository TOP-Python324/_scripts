from collections.abc import Iterable


class FixedList(list):
    def __init__(self, iterable: Iterable, *, max_len: int):
        i = len(iterable) - max_len
        i = i if i > 0 else 0
        iterable = tuple(iterable)[i:]
        super().__init__(iterable)
        self.max_len = max_len
    
    def append(self, object_):
        if len(self) == self.max_len:
            del self[0]
        super().append(object_)
    
    def insert(self, index: int, object_):
        if len(self) == self.max_len:
            del self[0]
            index -= 1
        super().insert(index, object_)
        # raise NotImplementedError
    
    def extend(self, iterable: Iterable):
        i = len(self) + len(iterable) - self.max_len
        i = i if i > 0 else 0
        del self[:i]
        super().extend(iterable)

