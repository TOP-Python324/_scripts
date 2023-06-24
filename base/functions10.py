def list_printer(list_: list) -> None:
    print(f'{id(list_)=}')
    list_[0] = 1000
    print(' '.join(str(elem) for elem in list_))
    


numbers = [1, 2, 3, 4, 5]

print(f'{id(numbers)=}')
list_printer(numbers)

print(numbers)

