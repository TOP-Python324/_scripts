text = input('текст: ')
i, j = int(input('i = ')), int(input('j = '))

text_listed = list(text)
print(type(text_listed), text_listed, sep='\n')

text_tupled = tuple(text)
print(type(text_tupled), text_tupled, sep='\n')

print(f'\n{text_listed[i:j] = }')
print(f'\n{text_tupled[j:i:-2] = }')
