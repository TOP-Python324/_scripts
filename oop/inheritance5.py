class Vehicle:
    wheels: int = 4
    
    def __init__(self, average_speed: int):
        self.speed = average_speed
    
    def move(self) -> str:
        return f'{self.__class__.__name__} moves on the ground with average speed of {self.speed} km/h'


class Bicycle(Vehicle):
    wheels = 2


class Car(Vehicle):
    pass


class Train(Vehicle):
    wheels = 16
    
    def move(self) -> str:
        return super().move().replace('on ground', 'along railroads')


# пример неудачного наследования — нарушение Принципа Подстановки Лисков
class Airplane(Vehicle):
    chassis: int = 3
    
    def __init__(self, average_ground_speed: int, average_air_speed: int):
        self.ground_speed = average_ground_speed
        self.air_speed = average_air_speed
    
    def move(self) -> str:
        return f'On the ground {self.__class__.__name__} moves with average speed of {self.ground_speed} km/h while in the air it flies with average speed of {self.air_speed} km/h'



def sort_by_speed(*vehicles: Vehicle) -> list[Vehicle]:
    return sorted(vehicles, key=lambda elem: elem.speed)


# >>> b1 = Bicycle(16)
# >>> b2 = Bicycle(24)
# >>> c1 = Car(73)
# >>> c2 = Car(80)
# >>> a1 = Airplane(50, 680)
# >>>
# >>> sort_by_speed(a1, c2, b1, b2, c1)
# ...
# AttributeError: 'Airplane' object has no attribute 'speed'

