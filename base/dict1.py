test_dict = {3: 'abc', 'AZ': [1, 2, 3], 0.01: 295}

print(f'{type(test_dict)}\n{test_dict}\n{len(test_dict) = }\n')

print(f'{test_dict[3] = }')
print(f'{test_dict["AZ"] = }')
print(f'{test_dict[0.01] = }\n')


# ключи не могут быть изменямыми объектами
# key = [1, 2]
# test_dict = {key: 'foobar'}

# key[0] = 100

# key_from_somewhere = [1, 2]
# приведёт к KeyError
# test_dict[key_from_somewhere]


letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

test_dict2 = dict(enumerate(letters, 1))
print(test_dict2, end='\n\n')

test_dict3 = {char: i for i, char in enumerate(letters, 1)}
# то же самое
# test_dict3 = {value: key for key, value in test_dict2.items()}
print(test_dict3, end='\n\n')


test_dict4 = dict.fromkeys(letters)
test_dict5 = dict.fromkeys(letters, 0.0)
# то же самое
# test_dict4 = {}.fromkeys(letters)
print(test_dict4, test_dict5, '', sep='\n\n')


