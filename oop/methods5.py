class Hero:
    def __init__(self, name: str, lvl: int, health: int):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.inventory: list[str] = []
        self.skills: list[str] = []
    
    def __iter__(self):
        return iter(self.inventory)
    
    def __contains__(self, skill: str):
        return skill in self.skills


ilya = Hero('Илья-Муромец', 30, 500)
ilya.inventory.extend((
    'меч',
    'лошадь'
))
ilya.skills.extend((
    'лежать на печи',
    'бить вражину'
))

# >>> for item in ilya:
# ...     print(item)
# ...
# меч
# лошадь
# >>>
# >>> list(ilya)
# ['меч', 'лошадь']
# >>>
# >>> print(*ilya)
# меч лошадь
# >>> 
# >>> 'лежать на печи' in ilya
# True
