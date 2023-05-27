if 10 == 1:
    print('равны')
elif 10 < 1:
    print('меньше')
elif 1 > 5:
    print('больше')
elif 'ab' != 'ab':
    print('не равны')
else:
    print('не шмогла')


text = input(' введи уже что-нибудь: ')
if text == '1':
    number = int(text)
    print(type(number))
else:
    print('фигня какая-то, а не число')


print('конец')
