# для имени класса используется ВерблюжийРегистр (CamelCase)
class TestClass:
    # атрибут класса
    a = 1
    # атрибут класса
    def func():
        return 'вызов завершён'


# >>> TestClass
# <class '__main__.TestClass'>
# >>>
# >>> TestClass.a
# 1
# >>>
# >>> TestClass.func
# <function TestClass.func at 0x000001F647BE2CA0>
# >>>
# >>> TestClass.func()
# 'вызов завершён'

# внутреннее пространство имён объекта класса
# >>> print(*(f'{k}: {v!r}' for k, v in TestClass.__dict__.items()), sep='\n')
# __module__: '__main__'
# a: 1
# func: <function TestClass.func at 0x000001F647BE2CA0>
# __dict__: <attribute '__dict__' of 'TestClass' objects>
# __weakref__: <attribute '__weakref__' of 'TestClass' objects>
# __doc__: None

# >>> print(*(f'{k}: {v!r}' for k, v in TestClass.__dict__.items() if not k.endswith('__')), sep='\n')
# a: 1
# func: <function TestClass.func at 0x000001F647BE2CA0>


# >>> t1 = TestClass()
# >>> t1
# <__main__.TestClass object at 0x000001F647C30C50>
# >>>
# >>> t1.__class__ is type(t1) is TestClass
# True

# внутреннее пространство имён экземпляра
# >>> t1.__dict__
# {}
# >>>
# >>> t1.a
# 1

# область видимости экземпляра расширяется до пространства имён объекта класса
# >>> print(*(a for a in dir(t1) if a in t1.__dict__ or a in TestClass.__dict__), sep='\n')
# __dict__
# __doc__
# __module__
# __weakref__
# a
# func

# атрибут b отсутствует в области видимости экземпляра
# >>> t1.b
# ...
# AttributeError: 'TestClass' object has no attribute 'b'

# добавление атрибута экземпляра
# >>> t1.b = 'instance attribute'
# >>>
# >>> t1.__dict__
# {'b': 'instance attribute'}

# >>> print(*(f'{k}: {v!r}' for k, v in TestClass.__dict__.items() if not k.endswith('__')), sep='\n')
# a: 1
# func: <function TestClass.func at 0x0000029C4FC22CA0>

# >>> print(*(a for a in dir(t1) if a in t1.__dict__ or a in TestClass.__dict__), sep='\n')
# __dict__
# __doc__
# __module__
# __weakref__
# a
# b
# func


# >>> t2 = TestClass()
# >>>
# >>> t2.__dict__
# {}
# >>>
# >>> t2.a = 1000
# >>> t2.a
# 1000
# >>>
# >>> t2.__dict__
# {'a': 1000}
# >>>
# >>> t2.__class__.a
# 1

