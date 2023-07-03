from pathlib import Path
from sys import path


for p in path:
    print(p)

# регистр для условных констант UPPER_SNAKE_CASE
USERS_DIR = Path(r'G:\Users')
SCRIPT_DIR = Path(path[0])
CWD = Path.cwd()

# >>> SCRIPT_DIR
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web/324/scripts/base')

# >>> CWD
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web/324/scripts/base')


print(SCRIPT_DIR, CWD, sep='\n')

# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base
#  15:54:57 > python path2.py
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base

# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web
#  15:54:57 > python 324\scripts\base\path2.py
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web
