names = []
prompt = 'введите имя: '

names += [input(prompt)]
# names = names + [input(prompt)]
names += [input(prompt)]
names += [input(prompt)]

string = ''.join(names)
print(string)

string = ' '.join(names)
print(string)

string = ' # '.join(names)
print(string)

string = ',\n'.join(names)
print(string)

