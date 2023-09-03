from itertools import chain
from string import ascii_letters as en_letters, digits, whitespace
from typing import Literal


ru_letters = ''.join(chr(code) for code in chain(range(1040, 1104), (1025, 1105)))
letters = {
    'en': en_letters,
    'ru': ru_letters,
}


class TextProcessor:
    """
    Позволяет извлекать список уникальных слов из текста и зашифровывать текст, используя шифр Цезаря.
    """
    codes = (
        range(65, 91),
        range(97, 123),
        range(1040, 1072),
        range(1072, 1104),
    )
    
    def __init__(self, text: str, lang: Literal['en', 'ru'] = 'en'):
        self.text = text
        self.punctuation: str = ''.join(
            set(text) - set(letters[lang]) - set(digits) - set(whitespace)
        )
    
    def unique_words(self) -> list[str]:
        """Возвращает отсортированный по алфавиту список уникальных слов, переведённых в нижний регистр."""
        return sorted({
            word.strip(self.punctuation).lower() 
            for word in self.text.split()
        })
    
    @classmethod
    def letter_range(cls, char: str) -> range | None:
        """Возвращает алфавитно-регистровый диапазон кодов UTF-8 для переданного буквенного символа. Если символ не входит ни в один из используемых классом диапазонов, то возвращает None."""
        code = ord(char)
        for range_ in cls.codes:
            if code in range_:
                return range_
    
    @staticmethod
    def shift(char: str, alphabet: range, shift: int) -> str:
        """Возвращает символ, сдвинутый по алфавиту alphabet от символа char на shift символов."""
        return chr((ord(char) - alphabet[0] + shift) % len(alphabet) + alphabet[0])
    
    def caesar(self, shift: int) -> str:
        """Возвращает текст, все буквенные символы которого сдвинуты по алфавиту на shift символов."""
        return ''.join(
            self.shift(ch, r, shift) if (r := self.letter_range(ch)) else ch
            for ch in self.text.replace('ё', 'е').replace('Ё', 'Е')
        )



text = '''Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.'''

tp = TextProcessor(text)
