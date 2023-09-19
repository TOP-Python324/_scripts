from decimal import Decimal as dec


class Person:
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str, 
    ):
        print(self)
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name


class Employee(Person):
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str, 
            position: str, 
            income: dec | int | str, 
    ):
        print(self)
        
        # нежелательно — явное использование родительского класса
        # Person.__init__(self, last_name, first_name, patr_name)
        
        # предпочтительно — создание прокси-экземпляра, с гибким поиском нужного атрибута в пространствах имён базовых классов
        super().__init__(last_name, first_name, patr_name)
        
        self.position = position
        self.income: dec = dec(income)


# >>> anna = Person('Демидова', 'Анна', 'Олеговна')
# <__main__.Person object at 0x000001F05000EB50>
# >>> 
# >>> anna.__dict__
# {'last_name': 'Демидова', 'first_name': 'Анна', 'patr_name': 'Олеговна'}

# >>> olga = Employee('Балашова', 'Ольга', 'Николаевна', 'специалист кадровой службы', 45000)
# <__main__.Employee object at 0x000001F05000EB10>
# <__main__.Employee object at 0x000001F05000EB10>
# >>> 
# >>> olga.__dict__
# {'last_name': 'Балашова', 'first_name': 'Ольга', 'patr_name': 'Николаевна', 'position': 'специалист кадровой службы', 'income': Decimal('45000')}


