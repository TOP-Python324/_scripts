# ТОЛЬКО ДЛЯ ДЕМОНСТРАЦИИ — на практике анонимные функции не должны явно присваиваться в переменные
anonim_func = lambda: 'возвращаемое значение'

print(type(anonim_func))
print(anonim_func)

# <class 'function'>
# <function <lambda> at 0x000002D9D4132D40>

# >>> anonim_func.__name__
# '<lambda>'

# >>> anonim_func()
# 'возвращаемое значение'


# >>> (lambda: 1 + 6)()
# 7


# ТОЛЬКО ДЛЯ ДЕМОНСТРАЦИИ — на практике анонимные функции не должны явно присваиваться в переменные
sqrt = lambda x: round(x**0.5)

# >>> sqrt(25)
# 5
# >>> sqrt(50)
# 7
# >>> sqrt()
# TypeError: <lambda>() missing 1 required positional argument: 'x'

