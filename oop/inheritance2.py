from pprint import pprint


class Parent:
    attr = 'value'


class Child(Parent):
    # переопределение атрибута
    attr = 'new value'


# >>> Child.attr
# 'new value'
# >>>
# >>> Parent.attr
# 'value'
# >>>
# >>> pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
              # 'attr': 'value',
              # '__dict__': <attribute '__dict__' of 'Parent' objects>,
              # '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
              # '__doc__': None})
# >>>
# >>> pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__', 'attr': 'new value', '__doc__': None})
# >>>
# >>> pprint(dir(Child), sort_dicts=False)
# ['__class__',
 # '__delattr__',
 # '__dict__',
 # '__dir__',
 # '__doc__',
 # '__eq__',
 # '__format__',
 # '__ge__',
 # '__getattribute__',
 # '__getstate__',
 # '__gt__',
 # '__hash__',
 # '__init__',
 # '__init_subclass__',
 # '__le__',
 # '__lt__',
 # '__module__',
 # '__ne__',
 # '__new__',
 # '__reduce__',
 # '__reduce_ex__',
 # '__repr__',
 # '__setattr__',
 # '__sizeof__',
 # '__str__',
 # '__subclasshook__',
 # '__weakref__',
 # 'attr']

