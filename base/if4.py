text = input(' ввод: ')


if text.startswith('команда1'):
    if text.endswith('10'):
        a = 10
        print(2**a)
    # else:
        # print(' _ неизвестная команда _ ')
else:
    print(' _ неизвестная команда _ ')


if text.startswith('команда1') and text.endswith('10'):
    a = 10
    print(2**a)
else:
    print(' _ неизвестная команда _ ')


print()

(
        print('левый операнд') != None 
    and print('центральный операнд') != None 
    and print('правый операнд') != None
)


