class Person:
    def __init__(self, name: str):
        self._name = name
    
    # геттер
    @property
    def name(self) -> str:
        return self._name
    
    # сеттер
    # def set_name(self, new_name: str) -> None:
    @name.setter
    def name(self, new_name: str) -> None:
        if isinstance(new_name, str):
            if new_name.isalpha():
                self._name = new_name
            else:
                raise ValueError("'new_name' must contain only letters")
        else:
            raise TypeError("'new_name' must be str")


ivan = Person('Иван')


# до использования свойств

# >>> ivan.set_name(248)
# ...
# TypeError: 'new_name' must be str
# >>>
# >>> ivan.set_name('248')
# ...
# ValueError: 'new_name' must contain only letters
# >>>
# >>> ivan.set_name('Афоня')
# >>>
# >>> ivan.name()
# 'Афоня'
# >>>
# >>> ivan._name
# 'Афоня'
# >>> ivan._name = 248
# >>>
# >>> ivan.__dict__
# {'_name': 248}


# после использования свойств

# >>> ivan.name = 101
# ...
# TypeError: 'new_name' must be str
# >>>
# >>> ivan.name = '<=ИВАНИЩЕ=>'
# ...
# ValueError: 'new_name' must contain only letters
# >>>
# >>> ivan.name = 'Афоня'
# >>> ivan.name
# 'Иван'
# >>>
# >>> ivan.name = 'Афоня'
# >>>
# >>> ivan.__dict__
# {'_name': 'Афоня'}
# >>>
# >>> ivan._name
# 'Афоня'
# >>> ivan._name = 101
# >>>
# >>> ivan.__dict__
# {'_name': 101}
