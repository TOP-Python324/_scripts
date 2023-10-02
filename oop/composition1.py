from enum import Enum
from random import choice
from typing import Self, Literal


class Person:
    
    class SEX(Enum):
        M = 'мужской'
        F = 'женский'
    
    def __init__(
            self, 
            last_name: str, 
            first_name: str, 
            patr_name: str,
            sex: Literal['мужской', 'женский'],
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
        self.sex: self.SEX = self.SEX(sex)
    
    def __repr__(self):
        intr = 'г-н' if self.sex is self.SEX.M else 'г-жа'
        return f'{intr} {self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'



