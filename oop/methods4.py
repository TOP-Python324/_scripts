class Fridge:
    def __init__(self):
        self.camera: list[str] = []
    
    def __iter__(self):
        return self.camera.__iter__()


fr1 = Fridge()
fr1.camera = ['молоко', 'курица']

# >>> for pr in fr1:
# ...     print(pr)
# ...
# молоко
# курица
