from datetime import date, datetime as dt, timedelta as td


default_date_format = '%d.%m.%y'


class Product:
    def __init__(
            self, 
            name: str, 
            produced: date | str = date.today(),
            expiration: int = 7, 
    ):
        self.name = name
        if isinstance(produced, str):
            produced = dt.strptime(produced, default_date_format).date()
        self.produced: date = produced
        self.expire: date = produced + td(days=expiration)
    
    def is_expired(self) -> bool:
        return self.expire <= date.today()
    
    def __repr__(self):
        return f'<{self.name.upper()}: {self.produced:{default_date_format}} – {self.expire:{default_date_format}}>'


class Fridge:
    def __init__(self):
        self.camera: list[Product] = []
    
    def clear_expired(self):
        for product in self.camera:
            if product.is_expired():
                self.camera.remove(product)
    
    def __iter__(self):
        return self.camera.__iter__()
    
    def __repr__(self):
        return '\n'.join(repr(pr) for pr in self.camera)



# >>> Product('молоко')
# <МОЛОКО: 16.09.23 – 23.09.23>

# >>> Product('сыр', '10.09.23', 30)
# <СЫР: 10.09.23 – 10.10.23>


kitchen = Fridge()

kitchen.camera.extend((
    Product('курица', '15.09.23', 2),
    Product('хлеб', '14.09.23', 5),
    Product('сметана', '12.09.23', 14),
    Product('лук', '25.07.23', 30),
))

# >>> kitchen
# <КУРИЦА: 15.09.23 – 17.09.23>
# <ХЛЕБ: 14.09.23 – 19.09.23>
# <СМЕТАНА: 12.09.23 – 26.09.23>
# <ЛУК: 25.07.23 – 24.08.23>
# >>>
# >>> kitchen.clear_expired()
# >>>
# >>> kitchen
# <КУРИЦА: 15.09.23 – 17.09.23>
# <ХЛЕБ: 14.09.23 – 19.09.23>
# <СМЕТАНА: 12.09.23 – 26.09.23>
