from datetime import date, datetime as dt


class Person:
    def __init__(self, name: str, birthdate: date | str):
        self.name = name
        if isinstance(birthdate, str):
            birthdate = dt.strptime(birthdate, '%d.%m.%Y').date()
        self.birthdate = birthdate
    
    # self < other
    def __lt__(self, other):
        # если операция сравнения должна проводиться только для экземпляров текущего класса:
        # try:
        #     return self.birthdate > other.birthdate
        # except AttributeError:
        #     raise TypeError(f"'<' not supported between instances of {self.__class__.__name__!r} and {other.__class__.__name__!r}")
        
        if isinstance(other, self.__class__):
            return self.birthdate > other.birthdate
        elif isinstance(other, int):
            return (date.today() - self.birthdate).days // 365.25 < other
    
    def __eq__(self, other):
        return self.birthdate == other.birthdate


ivan = Person('Иван', '01.01.2000')
zahar = Person('Захар', '23.11.1972')

# ivan < zahar
# ivan.__lt__(zahar) -> True

# zahar > ivan
# zahar.__gt__(ivan) .. TypeError
# ivan.__lt__(zahar) -> True

# ivan == zahar
# ivan.__eq__(zahar) -> False

# ivan != zahar
# ivan.__ne__(zahar) .. TypeError
# not ivan.__eq__(zahar) -> True

# ivan <= zahar
# ivan.__le__(zahar) .. TypeError
# zahar.__ge__(ivan) .. TypeError

# >>> ivan < 20
# False
# >>>
# >>> ivan < 25
# True
