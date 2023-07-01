a = 12

def test(param=0):
    print(f'\n{a = }')
    # локальные пространства имён функций test2() и test() не пересекаются 
    # print(f'\n{message = }')
    print('текущее пространство имён')
    print(locals())


def test2(message: str):
    test(123)
    print('текущее пространство имён')
    print(locals())


print('\nглобальное пространство имён')
print(globals())

test()

test2('')

print('\nтекущее пространство имён')
print(locals())

