class Knife:
    def cut():
        print('резать')
    
    def stab(self):
        print('колоть')


# >>> Knife.cut
# <function Knife.cut at 0x000001AEA1502CA0>
# >>>
# >>> Knife.stab
# <function Knife.stab at 0x000001AEA154F7E0>

# >>> kn1 = Knife()
# >>>
# >>> kn1.cut
# <bound method Knife.cut of <__main__.Knife object at 0x000001AEA1550CD0>>
# >>>
# >>> kn1.stab
# <bound method Knife.stab of <__main__.Knife object at 0x000001AEA1550CD0>>

# kn1.stab() --> Knife.stab(kn1)
# instance.method() --> instance.__class__.method(instance)

# >>> kn1.cut()
# ...
# TypeError: Knife.cut() takes 0 positional arguments but 1 was given

