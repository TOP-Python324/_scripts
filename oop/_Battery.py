class Battery(int):
    def __new__(cls, value: int, capacity: int):
        # instance = int.__new__(cls, value)
        instance = super().__new__(cls, value)
        instance.capacity = capacity
        return instance
    
    def __iadd__(self, other):
        # return Battery(super().__add__(other), self.capacity)
        return self.__class__(super().__add__(other), self.capacity)
    
    def __bool__(self):
        return self >= self.capacity


def strong_password(password: str) -> bool:
    validators = {
        'length': Battery(0, 8),
        'latin_upper': Battery(0, 1),
        'latin_lower': Battery(0, 1),
        'digits': Battery(0, 2),
        'others': Battery(0, 1)
    }
    for char in password:
        code = ord(char)
        validators['length'] += 1
        if 65 <= code <= 90:
            validators['latin_upper'] += 1
        elif 97 <= code <= 122:
            validators['latin_lower'] += 1
        elif 48 <= code <= 57:
            validators['digits'] += 1
        else:
            validators['others'] += 1
    return all(validators.values())

