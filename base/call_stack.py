def func6():
    print('последний вызов')

def func5():
    print('пятый вызов')
    func6()
    print('возврат из пятого вызова')

def func4():
    print('четвёртый вызов')
    func5()
    print('возврат из четвёртого вызова')

def func3():
    print('третий вызов')
    func4()
    print('возврат из третьего вызова')

def func2():
    print('второй вызов')
    func3()
    print('возврат из второго вызова')

def func1():
    print('первый вызов')
    func2()
    print('возврат из первого вызова')


func1()

# полностью заполненный стек вызовов функций: перед выводом 'последний вызов'
# <module>
# func1()
# func2()
# func3()
# func4()
# func5()
# func6()
