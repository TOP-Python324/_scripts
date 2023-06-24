def test_generator_func() -> 'generator':
    """Генераторная функция."""
    print('начало выполнения тела генераторной функции')
    yield 1
    print('продолжение выполнения тела генераторной функции')
    yield 2
    print('конец выполнения тела генераторной функции')


generator_obj = test_generator_func()
print(type(generator_obj))
print(generator_obj, end='\n\n')


print(generator_obj.__next__())
print(generator_obj.__next__())
try:
    print(generator_obj.__next__())
except StopIteration:
    pass

# сразу же выбросит StopIteration
for elem in generator_obj:
    print(elem)

# сразу же выбросит StopIteration
print(list(generator_obj))

# создание нового объекта генератора
for elem in test_generator_func():
    print(elem)

