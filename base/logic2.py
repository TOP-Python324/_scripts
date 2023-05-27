text1 = input(' первая строка: ')
text2 = input(' вторая строка: ')

print(f'\n{text1 == text2 = }')
print(f'{text1 != text2 = }\n')

print(f'{text1 < text2 = }')
print(f'{text1 > text2 = }\n')

if text1.isdecimal() and text2.isdecimal():
    print(f'{int(text1) < int(text2) = }')
    print(f'{int(text1) > int(text2) = }\n')

