from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from sys import modules

# путь к файлу
file_path = Path('1.py')
# имя будущего объекта модуля
module_name = 'module: 1.py'

# создание объекта спецификации
spec = spec_from_file_location(module_name, file_path)
# создание объекта модуля
param_pam_pam = module_from_spec(spec)
# добавление объекта модуля в словарь модулей
modules[module_name] = param_pam_pam
# выполнение кода в объекте модуля
spec.loader.exec_module(param_pam_pam)


print(type(param_pam_pam))
print(param_pam_pam)

