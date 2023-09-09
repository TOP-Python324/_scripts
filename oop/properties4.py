class User:
    def __init__(self, login: str, email: str, password: str):
        self.login = login
        self._email = email
        self.__password: int = hash(password)
    
    # геттер должен быть объявлен, но не обязан вовзвращать значение
    @property
    def password(self) -> None:
        # return None
        raise NotImplementedError
    
    # сеттер не может быть объявлен без геттера
    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = hash(new_password)
    
    def authorize(self, password: str) -> bool:
        return self.__password == hash(password)


genndalf = User('GennDALF', 'Genn.DALF@ya.ru', 'qwerty')

# >>> genndalf.password
# ...
# NotImplementedError
# >>>
# >>> genndalf.password = 'new passw 3'
# >>>
# >>> genndalf.authorize('qwerty')
# False
# >>> genndalf.authorize('new passw 3')
# True
