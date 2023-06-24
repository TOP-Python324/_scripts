def map(func_obj: 'callable', iterator: 'iterable') -> list:
    """Упрощённый аналог встроенной функции map()"""
    result = []
    for elem in iterator:
        result += [func_obj(elem)]
    return result
    

def punctuation_stripper(word: str) -> str:
    """Возвращает объект str с удалёнными символами пунктуации по краям."""
    return word.strip('.,:;!?()\'\"-–—')


def caesar_coder(word: str, shift: int = 1) -> str:
    """Возвращает объект str с буквенными символами, сдвинутыми на shift в пределах латинского алфавита."""
    result = ''
    for char in word.lower():
        if char.isalpha():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def is_capitalized(word: str) -> bool:
    return word[:1].isupper()


text = '''Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)'''


# >>> map(punctuation_stripper, text.split())
# ['Operations', 'and', 'built-in', 'functions', 'that', 'have', 'a', 'Boolean', 'result', 'always', 'return', '0', 'or', 'False', 'for', 'false', 'and', '1', 'or', 'True', 'for', 'true', 'unless', 'otherwise', 'stated', 'Important', 'exception', 'the', 'Boolean', 'operations', 'or', 'and', 'and', 'always', 'return', 'one', 'of', 'their', 'operands']

# >>> map(caesar_coder, text.split())
# ['pqfsbujpot', 'boe', 'cvjmu-jo', 'gvodujpot', 'uibu', 'ibwf', 'b', 'cppmfbo', 'sftvmu', 'bmxbzt', 'sfuvso', '0', 'ps', 'gbmtf', 'gps', 'gbmtf', 'boe', '1', 'ps', 'usvf', 'gps', 'usvf,', 'vomftt', 'puifsxjtf', 'tubufe.', '(jnqpsubou', 'fydfqujpo:', 'uif', 'cppmfbo', 'pqfsbujpot', 'ps', 'boe', 'boe', 'bmxbzt', 'sfuvso', 'pof', 'pg', 'uifjs', 'pqfsboet.)']

# >>> words = text.split()
# >>> capped = map(is_capitalized, words)
# >>> coded = map(caesar_coder, words)
# >>>
# >>> text_coded = ' '.join(word.capitalize() if capped[i] else word for i, word in enumerate(coded))
# >>> text_coded
# 'Pqfsbujpot boe cvjmu-jo gvodujpot uibu ibwf b Cppmfbo sftvmu bmxbzt sfuvso 0 ps Gbmtf gps gbmtf boe 1 ps Usvf gps usvf, vomftt puifsxjtf tubufe. (jnqpsubou fydfqujpo: uif Cppmfbo pqfsbujpot ps boe boe bmxbzt sfuvso pof pg uifjs pqfsboet.)'
