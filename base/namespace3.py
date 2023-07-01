var = 'глобальная переменная'


def external():
    var = 'локальная переменная external'
    
    def internal():
        # var = 'локальная переменная internal'
        # global var
        nonlocal var
        var = 10000
    
    internal()
    print(var)


external()
print(var)
