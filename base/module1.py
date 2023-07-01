"""
Модуль 1: точка входа.
"""
print(f'начало выполнения модуля {__name__}')

import module2

var1 = 'глобальная переменная'

print('\nглобальное пространство имён (без встроенных атрибутов)')
print({k: v for k, v in globals().items() if not k.startswith('__')})

print('\nвнутреннее пространство имён объекта модуля (без встроенных атрибутов)')
print({k: v for k, v in module2.__dict__.items() if not k.startswith('__')})


print(f'\nконец выполнения модуля {__name__}')


# >>> module2
# <module 'module2' from 'D:\\G-Doc\\YandexDisk\\Job\\TOP Academy\\Python web\\324\\scripts\\base\\module2.py'>

# >>> type(module2)
# <class 'module'>

# >>> module2.ab
# 200

# >>> module2.ab = 'new object'
# >>> module2.ab
# 'new object'

# >>> module2.module3.no = [1, 2, 3]
# >>> module2.module3.no
# [1, 2, 3]

# >>> module2.module3.no[0] = 1000
# >>> module2.module3.no
# [1000, 2, 3]
