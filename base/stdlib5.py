from re import compile

email_pattern = compile(r'[a-zA-Z0-9]\w*@[a-zA-Z][\w\.]+\.[a-zA-Z]{2,4}')

email = input(' введите email: ')
if email_pattern.fullmatch(email):
    print('email коррректный')
else:
    print('email некоррректный')
