from decimal import Decimal as dec
from numbers import Number, Real


print(f'{0.1 + 0.1 + 0.1 == 0.3 = }\n')

print(dec(0.1), dec(0.1), dec(0.1), dec(0.3), '', sep='\n')


print(f"{dec('0.1') + dec('0.1') + dec('0.1') == dec('0.3') = }\n")


print(f'{isinstance(dec(4), Number) = }')
print(f'{isinstance(dec(4), Real) = }\n')

# >>> dec(4) + 4
# Decimal('8')
# >>>
# >>> dec('2.2') + 1
# Decimal('3.2')
# >>>
# >>> dec('2.2') + 2.2
# ...
# TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'


# >>> temperature = 36.7
# >>> 
# >>> dec(temperature)
# Decimal('36.7000000000000028421709430404007434844970703125')
# >>>
# >>> str(temperature)
# '36.7'
# >>>
# >>> dec(str(temperature))
# Decimal('36.7')
