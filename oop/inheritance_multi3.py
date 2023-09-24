from collections.abc import Iterable


class Printable:
    def print(self) -> None:
        print('\n'.join(
            f'{attr}: {value!r}'
            for attr, value in self.__dict__.items()
        ))



class Person:
    def __init__(self, last_name: str, first_name: str, patr_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    def __repr__(self):
        return f'{self.first_name} {self.patr_name} {self.last_name}'


class Student(Person, Printable):
    def __init__(self, last_name: str, first_name: str, patr_name: str, year: int):
        super().__init__(last_name, first_name, patr_name)
        self.year = year



class CatalogueCard:
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year


class BookCard(CatalogueCard):
    def __init__(self, title: str, year: int, author: Person, *authors: Person):
        super().__init__(title, year)
        self.authors: tuple[Person, ...] = author, *authors


class CompendiumCard(CatalogueCard, dict, Printable):
    def __init__(self, title: str, year: int, articles: dict[str, Iterable[Person]]):
        super().__init__(title, year) 
        super(CatalogueCard, self).__init__(articles)



# >>> CompendiumCard.__mro__
# (<class '__main__.CompendiumCard'>, <class '__main__.CatalogueCard'>, <class 'dict'>, <class '__main__.Printable'>, <class 'object'>)

# >>> vui = Person('Иванов', 'Владимир', 'Юрьевич')
# >>> enz = Person('Захаров', 'Евгений', 'Николаевич')
# >>> art1 = 'Исследование применения теории управления конечными автоматами в производстве РФП'
# >>> 
# >>> fti2020 = CompendiumCard(
# ...     'Летняя конференция ФТИ - 2020', 
# ...     2020,
# ...     {art1: [vui, enz]}
# ... )
# >>>
# >>> fti2020.print()
# title: 'Летняя конференция ФТИ - 2020'
# year: 2020
# >>>
# >>> fti2020
# {'Исследование применения теории управления конечными автоматами в производстве РФП': [Владимир Юрьевич Иванов, Евгений Николаевич Захаров]}
# >>> 
# >>> ank = Student('Козлов', 'Артём', 'Николаевич', 1)
# >>> oak = Student('Кузнецова', 'Олеся', 'Александровна', 1)
# >>>
# >>> ank.print()
# last_name: 'Козлов'
# first_name: 'Артём'
# patr_name: 'Николаевич'
# year: 1
# >>> oak.print()
# last_name: 'Кузнецова'
# first_name: 'Олеся'
# patr_name: 'Александровна'
# year: 1

