def filter(func_obj: 'callable', iterator: 'iterable') -> list:
    """Упрощённый аналог встроенной функции filter()"""
    result = []
    for elem in iterator:
        if func_obj(elem):
            result += [elem]
    return result


def is_long(word: str) -> bool:
    return len(word) > 3


def is_capitalized(word: str) -> bool:
    return word[:1].isupper()


cyrillic_codes = {1025, 1105} | set(range(1040, 1104))

def is_cyrillic(word: str) -> bool:
    for code in [ord(ch) for ch in word]:
        if code not in cyrillic_codes:
            return False
    else:
        return True


text = '''Operations and built-in functions that have a Boolean result always return 0 or Ложь for false and 1 or Истина for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)'''


# >>> filter(is_long, text.split())
# ['Operations', 'built-in', 'functions', 'that', 'have', 'Boolean', 'result', 'always', 'return', 'False', 'false', 'True', 'true,', 'unless', 'otherwise', 'stated.', '(Important', 'exception:', 'Boolean', 'operations', 'always', 'return', 'their', 'operands.)']

# >>> filter(is_cyrillic, text.split())
# ['Ложь', 'Истина']

# >>> filter(is_cyrillic, text)
# ['Л', 'о', 'ж', 'ь', 'И', 'с', 'т', 'и', 'н', 'а']
