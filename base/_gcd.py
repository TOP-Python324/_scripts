def gcd(num1: int, num2: int) -> int:
    """Возвращает наибольший общий делитель двух положительных чисел."""
    print(f'{num1=} {num2=}')
    if num2 == 0:
        return num1
    else:
        result = gcd(num2, num1 % num2)
        print(f'{result=}')
        return result


# >>> gcd(16, 12)
# num1=16 num2=12
# num1=12 num2=4
# num1=4 num2=0
# result=4
# result=4
# 4

# >>> gcd(121, 19)
# num1=121 num2=19
# num1=19 num2=7
# num1=7 num2=5
# num1=5 num2=2
# num1=2 num2=1
# num1=1 num2=0
# result=1
# result=1
# result=1
# result=1
# result=1
# 1
