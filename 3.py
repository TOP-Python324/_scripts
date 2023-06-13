total = 0
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

#Введите число: 50
#93

#Введите число: 82
#126