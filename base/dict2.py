from random import uniform


letter_weight = {'а': 0.0, 'б': 0.0, 'в': 0.0, 'г': 0.0, 'д': 0.0, 'е': 0.0, 'ё': 0.0, 'ж': 0.0, 'з': 0.0, 'и': 0.0, 'й': 0.0, 'к': 0.0, 'л': 0.0, 'м': 0.0, 'н': 0.0, 'о': 0.0, 'п': 0.0, 'р': 0.0, 'с': 0.0, 'т': 0.0, 'у': 0.0, 'ф': 0.0, 'х': 0.0, 'ц': 0.0, 'ч': 0.0, 'ш': 0.0, 'щ': 0.0, 'ъ': 0.0, 'ы': 0.0, 'ь': 0.0, 'э': 0.0, 'ю': 0.0, 'я': 0.0}
print(f'{id(letter_weight) = }\n')

# >>> list(letter_weight)
# ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for key in letter_weight:
    # print(repr(key), end=' ')
    letter_weight[key] = round(uniform(-0.5, 0.5), 1)
    print(f'{key!r}: {letter_weight[key]}', end=' ')
    
print(f'\n\n{id(letter_weight) = }\n')


for value in sorted(letter_weight.values()):
    print(value, end=' ')
print('\n')


for item in letter_weight.items():
    print(item, end=' ')
print('\n')

for key, value in letter_weight.items():
    new_val = value**2 + uniform(0, 0.2)
    
    letter_weight[key] = round(new_val, 2)
    print(f'{key!r}: {value} -> {new_val:.2f}')
    
print('\n')

