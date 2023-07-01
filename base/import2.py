import module2 as mod2

from module3 import no as mod3_no


print('\nглобальное пространство имён (без встроенных атрибутов)')
print({k: v for k, v in globals().items() if not k.startswith('__')})
