text = input('введите текст: ')

for i in range(1, len(text)):
    print(text[i-1:i+3])
print()

for i in range(0, len(text), 4):
    print(text[i:i+4])
print()

