class A:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор А')
        self.attr = 'атрибут A'


class B:
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор B')
        self.attr = 'атрибут B'


class C(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор C')
        super().__init__()


# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> c = C()
# >>>
# >>> c.attr
# 'атрибут A'


class E(A, B):
    def __init__(self):
        print(f'экземпляр {self.__class__.__name__}: конструктор E')
        super(A, self).__init__()


# >>> E.__mro__
# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> e = E()
# >>>
# >>> e.attr
# 'атрибут B'


class F:
    pass


class G(F, C, E):
    pass


# >>> G.__mro__
# (<class '__main__.G'>, <class '__main__.F'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>> 
# >>> g = G()
# экземпляр G: конструктор C
# экземпляр G: конструктор E
# экземпляр G: конструктор B
# >>> 
# >>> g.attr
# 'атрибут B'



# class E(B, A):
#     pass

# порядок наследования C конфликтует с порядком наследования E
# class G(F, C, E):
#     pass

# TypeError: Cannot create a consistent method resolution order (MRO) for bases object, A, B
