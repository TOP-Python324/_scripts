class Square:
    def __init__(self, side: float):
        self._side = float(side)
        self.__area = float(side**2)
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, new_side: float) -> None:
        self._side = float(new_side)
        self.__area = float(new_side**2)
    
    @property
    def area(self) -> float:
        return self.__area
    
    @area.setter
    def area(self, new_area: float) -> None:
        self._side = new_area**0.5
        self.__area = float(new_area)


sq1 = Square(5)

# >>> sq1.side
# 5.0
# >>> sq1.area
# 25.0
# >>>
# >>> sq1.side = 7
# >>> sq1.area
# 49.0
# >>>
# >>> sq1.area = 100
# >>> sq1.area
# 100.0
# >>> sq1.side
# 10.0
