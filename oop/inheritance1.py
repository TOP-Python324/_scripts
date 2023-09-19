from pprint import pprint


class Parent:
    attr = 'value'


class Child(Parent):
    pass


# внутреннее пространство имён объекта базового класса
# >>> pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
              # 'attr': 'value',
              # '__dict__': <attribute '__dict__' of 'Parent' objects>,
              # '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
              # '__doc__': None})

# внутреннее пространство имён объекта производного класса
# >>> pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__', 
              # '__doc__': None})

# полностью расширенная область видимости объекта производного класса
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

# >>> Child.attr
# 'value'

# порядок наследования: от текущего класса к базовым
# >>> Child.__mro__
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)

# >>> pprint(object.__dict__, sort_dicts=False)
# mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFE42418DF0>,
              # '__repr__': <slot wrapper '__repr__' of 'object' objects>,
              # '__hash__': <slot wrapper '__hash__' of 'object' objects>,
              # '__str__': <slot wrapper '__str__' of 'object' objects>,
              # '__getattribute__': <slot wrapper '__getattribute__' of 'object' objects>,
              # '__setattr__': <slot wrapper '__setattr__' of 'object' objects>,
              # '__delattr__': <slot wrapper '__delattr__' of 'object' objects>,
              # '__lt__': <slot wrapper '__lt__' of 'object' objects>,
              # '__le__': <slot wrapper '__le__' of 'object' objects>,
              # '__eq__': <slot wrapper '__eq__' of 'object' objects>,
              # '__ne__': <slot wrapper '__ne__' of 'object' objects>,
              # '__gt__': <slot wrapper '__gt__' of 'object' objects>,
              # '__ge__': <slot wrapper '__ge__' of 'object' objects>,
              # '__init__': <slot wrapper '__init__' of 'object' objects>,
              # '__reduce_ex__': <method '__reduce_ex__' of 'object' objects>,
              # '__reduce__': <method '__reduce__' of 'object' objects>,
              # '__getstate__': <method '__getstate__' of 'object' objects>,
              # '__subclasshook__': <method '__subclasshook__' of 'object' objects>,
              # '__init_subclass__': <method '__init_subclass__' of 'object' objects>,
              # '__format__': <method '__format__' of 'object' objects>,
              # '__sizeof__': <method '__sizeof__' of 'object' objects>,
              # '__dir__': <method '__dir__' of 'object' objects>,
              # '__class__': <attribute '__class__' of 'object' objects>,
              # '__doc__': 'The base class of the class hierarchy.\n'
                         # '\n'
                         # 'When called, it accepts no arguments and returns a '
                         # 'new featureless\n'
                         # 'instance that has no instance attributes and cannot '
                         # 'be given any.\n'})


