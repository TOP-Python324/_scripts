from itertools import *
from random import sample
from string import ascii_lowercase as letters


cnt = 0
for ch in cycle('PYTHON'):
    print(ch, end='')
    cnt += 1
    if cnt >= 70:
        break
print('\n')


numbers = sample(range(10, 100), 10)
rand_word = ''.join(sample(letters, 5))
signs = set('-+*/')
for elem in chain(numbers, rand_word, signs):
    print(elem, end=' ')
print('\n')


print(list(filter(lambda x: x < 50, numbers)))
print(list(filterfalse(lambda x: x < 50, numbers)), end='\n\n')


rand_word2 = ''.join(sample(letters, 7))
for ch1, ch2 in zip(rand_word, rand_word2):
    print(ch1, ch2)
print()

for ch1, ch2 in zip_longest(rand_word, rand_word2, fillvalue=' '):
    print(ch1, ch2)
print()
