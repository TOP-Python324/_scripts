b = []
while True:
    numb = int(input("Введите число: "))
    if numb % 7 != 0:
        break
    else:
        b.append(numb)
print(*reversed(b))

#Введите число: 7
#Введите число: 14
#Введите число: 21
#Введите число: 28
#Введите число: 1

#28 21 14 7
