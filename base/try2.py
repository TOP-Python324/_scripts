prompt = ' введите число > '
try:
    num1, num2 = int(input(prompt)), int(input(prompt))
    result = num1 / num2
# перехват исключений только указанного типа
except ZeroDivisionError:
    print('на ноль не делим')


try:
    num1, num2 = int(input(prompt)), int(input(prompt))
    result = num1 / num2
# перехват исключений любого из перечисленных типов
except (ZeroDivisionError, ValueError):
    print('ошибка')


try:
    num1, num2 = int(input(prompt)), int(input(prompt))
    result = num1 / num3
except ZeroDivisionError:
    print('на ноль не делим')
except ValueError:
    print('вводи только цифры')
except:
    print('ошибка')

