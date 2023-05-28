# строка
str_object = 'abcdef'
empty_str = ''

# >>> char = 'z'
# >>> type(char)
# <class 'str'>
# >>>
# >>> string = 'zz'
# >>> type(string)
# <class 'str'>

# список
list_object = [1, 2.2, '3', [4, 5]]
empty_list = []

# кортеж
tuple_object = (1, 2.2, '3', [4, 5])
empty_tuple = ()


print(len(str_object))
print(len(list_object))
print(len(tuple_object), end='\n\n')


ch1, ch2, ch3 = str_object[0], str_object[1], str_object[5]
print(ch1, ch2, ch3)
print(type(ch1), type(ch2), type(ch3), end='\n\n')

el1, el2, el3 = list_object[1], list_object[2], list_object[3]
print(el1, el2, el3)
print(type(el1), type(el2), type(el3), end='\n\n')

