class User:
    def __init__(self, login: str, email: str, password: str):
        # публичный
        self.login = login
        # частный
        self._email = email
        # защищённый
        self.__pass_hash: int = hash(password)
    
    def authorize(self, password: str) -> bool:
        return self.__pass_hash == hash(password)


genndalf = User('GennDALF', 'Genn.DALF@ya.ru', 'qwerty')


# >>> genndalf.__dict__
# {'login': 'GennDALF', '_email': 'Genn.DALF@ya.ru', '_User__pass_hash': -160188248185809044}


# >>> genndalf.login
# 'GennDALF'
# >>>
# >>> genndalf._email
# 'Genn.DALF@ya.ru'
# >>>
# >>> genndalf.__pass_hash
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'User' object has no attribute '__pass_hash'


# >>> genndalf._User__pass_hash
# -160188248185809044
# >>>
# >>> genndalf.login = 10
# >>>
# >>> genndalf._email = 20
# >>>
# >>> genndalf._User__pass_hash = 30
# >>>
# >>> genndalf.__dict__
# {'login': 10, '_email': 20, '_User__pass_hash': 30}


# >>> genndalf.authorize('qwerty')
# True
# >>>
# >>> genndalf.authorize('12345')
# False

