text = input(' ввод: ')


if text.startswith('команда1'):
    if text.endswith('10') or text.endswith('20') or text.endswith('30'):
        a = 10
        print(2**a)
    else:
        print(' _ неизвестный аргумент _ ')
else:
    print(' _ неизвестная команда _ ')


if (
        text.startswith('команда1') 
    and (text.endswith('10') or text.endswith('20') or text.endswith('30'))
):
    a = 10
    print(2**a)
else:
    print(' _ неизвестная команда _ ')


print()

(
       print('левый операнд') == None 
    or print('центральный операнд') == None 
    or print('правый операнд') == None
)

