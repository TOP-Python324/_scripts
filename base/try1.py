prompt = ' введите число > '
while True:
    try:
        num1, num2 = int(input(prompt)), int(input(prompt))
        result = num1 / num2
    except:
        print('ошибка')
        break
    else:
        print('безошибочно')
    finally:
        print()
