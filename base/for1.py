text = input('строка: ')

for char in text:
    print(char, type(char))
print()


words = text.split()

for word in words:
    print(word.upper())
print()

