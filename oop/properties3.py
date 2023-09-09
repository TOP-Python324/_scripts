class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self.__area = width * height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, new_value: int) -> None:
        self._width = new_value
        self.__area = new_value * self._height
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_value: int) -> None:
        self._height = new_value
        self.__area = self._width * new_value
    
    # геттер может быть объявлен без сеттера
    @property
    def area(self) -> int:
        return self.__area


rc1 = Rectangle(5, 10)

# >>> rc1.width
# 5
# >>> rc1.height
# 10
# >>> rc1.area
# 50
# >>> rc1.width = 12
# >>> rc1.area
# 120
# >>> rc1.area = 100
# ...
# AttributeError: property 'area' of 'Rectangle' object has no setter
