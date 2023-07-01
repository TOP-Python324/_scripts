var1 = 'глобальная переменная'
var2 = [1, 2, 3]


def namespaces():
    # global var1
    var1 = 122
    print(var1)
    
    var2[0] = 1000
    # print(id(var2))
    
    print(locals())
    # имена и объекты глобального просранства имён не считая встроенных (имена встроенных объектов начинаются и заканчиваются на '__')
    print({k: v for k, v in globals().items() if not k.startswith('__')})


# print(id(var2))

namespaces()

