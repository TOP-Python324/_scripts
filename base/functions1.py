def test_function():
    print('python is cool!')


print_return = print('после объявления функции')
test_func_return = test_function()
print(f'\n{print_return}\n{test_func_return}\n')


def test_function2():
    print('начало выполнения test_function2()')
    return 'python'*2
    # никогда не будет выполнено:
    # print('конец выполнения test_function2()')


test_func_return = test_function2()
print(f'{test_func_return}\n')


def run_command(command):
    if command == 'line':
        return '—'*79
    elif command == 'box':
        line = '—'*79 + '\n'
        empty = '|' + ' '*77 + '|\n'
        return (line + empty*3 + line).strip()
    

drawing = run_command('line')
print(drawing, end='\n\n')

drawing = run_command('box')
print(drawing, end='\n\n')

drawing = run_command('circle')
print(drawing, end='\n\n')

