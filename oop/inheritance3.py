class Proteus:
    @staticmethod
    def move():
        return 'движение'
    
    @staticmethod
    def eat():
        return 'питание'
    
    @staticmethod
    def reproduce():
        return 'размножение'


class Fish(Proteus):
    @staticmethod
    def breath():
        return 'дыхание'


class Reptile(Fish):
    @staticmethod
    def hide():
        return 'скрытность'


class Bird(Reptile):
    @staticmethod
    def fly():
        return 'полёт'


class Mammal(Reptile):
    @staticmethod
    def care():
        return 'забота'


class Human(Mammal):
    @staticmethod
    def speak():
        return 'речь'


# >>> ivan = Human()
# >>>
# >>> ivan.move()
# 'движение'
# >>> ivan.eat()
# 'питание'
# >>> ivan.breath()
# 'дыхание'
# >>> ivan.hide()
# 'скрытность'
# >>> ivan.fly()
# ... AttributeError: 'Human' object has no attribute 'fly'
# >>> ivan.care()
# 'забота'
# >>> ivan.speak()
# 'речь'
# >>> 
# >>> Human.__mro__
# (<class '__main__.Human'>, <class '__main__.Mammal'>, <class '__main__.Reptile'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)


# >>> lizzy = Reptile()
# >>>
# >>> lizzy.move()
# 'движение'
# >>> lizzy.eat()
# 'питание'
# >>> lizzy.breath()
# 'дыхание'
# >>> lizzy.hide()
# 'скрытность'
# >>> lizzy.fly()
# ... AttributeError: 'Reptile' object has no attribute 'fly'
# >>> lizzy.care()
# ... AttributeError: 'Reptile' object has no attribute 'care'
# >>> lizzy.speak()
# ... AttributeError: 'Reptile' object has no attribute 'speak'
# >>> 
# >>> lizzy.__class__.__mro__
# (<class '__main__.Reptile'>, <class '__main__.Fish'>, <class '__main__.Proteus'>, <class 'object'>)

