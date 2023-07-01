"""
Модуль 2: дополнительный.
"""
print(f'\tначало выполнения модуля {__name__}')

import module3


def check_global_namespace():
    print(globals())


ab = 200

print(f'\tконец выполнения модуля {__name__}')