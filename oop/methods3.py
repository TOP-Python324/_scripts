from random import randrange as rr


class Audit:
    def __init__(self, organization: str):
        self.organization = organization
        self.step1: bool = False
        self.step2: bool = False
        self.step3: bool = False
    
    def __run_check1(self) -> bool:
        return bool(rr(2))
    
    def __run_check2(self) -> bool:
        return bool(rr(2))
    
    def __run_check3(self) -> bool:
        return bool(rr(2))
    
    def __call__(self) -> bool:
        self.step1 = self.__run_check1()
        self.step2 = self.__run_check2()
        self.step3 = self.__run_check3()
        return all((self.step1, self.step2, self.step3))


sber_audit = Audit('Сбер')

# >>> sber_audit
# <__main__.Audit object at 0x0000028B21981150>
# >>> 
# >>> sber_audit.__dict__
# {'organization': 'Сбер', 'step1': False, 'step2': False, 'step3': False}
# >>> 
# >>> sber_audit()
# False
# >>> sber_audit.__dict__
# {'organization': 'Сбер', 'step1': True, 'step2': True, 'step3': False}
