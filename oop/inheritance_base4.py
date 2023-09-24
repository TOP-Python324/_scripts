

class Natural(int):
    def __new__(cls, value: int):
        if value <= 0:
            raise ValueError
        return super().__new__(cls, value)


class RangedNumber(int):
    def __new__(cls, value: int, left: int, right: int):
        if isinstance(value, int) and isinstance(left, int) and isinstance(right, int):
            if value < left:
                inst = super().__new__(cls, left)
            elif right < value:
                inst = super().__new__(cls, right)
            else:
                 inst = super().__new__(cls, value)
            inst.left = left
            inst.right = right
            return inst
        else:
            raise ValueError
    
    def __add__(self, other):
        return self.__class__(super().__add__(other), self.left, self.right)
    
    def __radd__(self, other):
        return self.__class__(super().__radd__(other), self.left, self.right)
    
    def __sub__(self, other):
        return self.__class__(super().__sub__(other), self.left, self.right)
    
    def __rsub__(self, other):
        return self.__class__(super().__rsub__(other), self.left, self.right)
    
    def __mul__(self, other):
        return self.__class__(super().__mul__(other), self.left, self.right)
    
    def __rmul__(self, other):
        return self.__class__(super().__rmul__(other), self.left, self.right)
    
    def __floordiv__(self, other):
        return self.__class__(super().__floordiv__(other), self.left, self.right)
    
    def __rfloordiv__(self, other):
        return self.__class__(super().__rfloordiv__(other), self.left, self.right)
    
    def __mod__(self, other):
        return self.__class__(super().__mod__(other), self.left, self.right)
    
    def __rmod__(self, other):
        return self.__class__(super().__rmod__(other), self.left, self.right)
    
    def __pow__(self, other):
        return self.__class__(super().__pow__(other), self.left, self.right)
    
    def __rpow__(self, other):
        return self.__class__(super().__rpow__(other), self.left, self.right)


