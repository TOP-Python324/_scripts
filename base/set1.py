test_set = {2, 2, 4, 5, 1, 2, 4, 8}

print(f'{type(test_set)}\n{test_set}\n{len(test_set)}\n')


text = '''Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering). Order comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise TypeError.'''

chars = set(text)
print(f'{chars}\n{len(chars)}\n')

punctuation = '.,‘’()<>= '
chars = {ch for ch in text if ch not in punctuation}

for ch in chars:
    print(ch, end='')
print(f'\n\nдо изменения: {id(chars) = }')

chars.add('z')
chars.remove('d')
# приведёт к KeyError
# chars.remove('x')
chars.discard('x')
chars.discard('q')

print(f'после изменения: {id(chars) = }\n')

chars_frost = frozenset(chars)
print(chars_frost, end='\n\n')

chars_frost.add('x')


