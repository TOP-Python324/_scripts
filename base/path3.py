from pathlib import Path
from sys import path


SCRIPT_DIR = Path(path[0])

# >>> SCRIPT_DIR.is_dir()
# True
# >>> SCRIPT_DIR.is_file()
# False
# >>>
# >>> SCRIPT_DIR.exists()
# True


file_path = SCRIPT_DIR / 'data/path1.py'

data_dir = Path('data')
file_path = SCRIPT_DIR / data_dir / '1.py'

# >>> file_path.exists()
# False
# >>> file_path.is_dir()
# False
# >>> file_path.is_file()
# False

group_dir = SCRIPT_DIR / '../..'

# >>> group_dir.is_dir()
# True

for obj in group_dir.iterdir():
    print(obj)

# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base\..\..\homeworks
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base\..\..\HW.txt
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base\..\..\logo.png
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base\..\..\Python324_журнал.xlsx
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts\base\..\..\scripts


# >>> SCRIPT_DIR.parent
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web/324/scripts')

# >>> SCRIPT_DIR.parent.name
# 'scripts'

# >>> SCRIPT_DIR.parent.parent
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web/324')

# >>> SCRIPT_DIR.parent.parent.name
# '324'


for p in SCRIPT_DIR.parents:
    print(p)

# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324\scripts
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web\324
# D:\G-Doc\YandexDisk\Job\TOP Academy\Python web
# D:\G-Doc\YandexDisk\Job\TOP Academy
# D:\G-Doc\YandexDisk\Job
# D:\G-Doc\YandexDisk
# D:\G-Doc
# D:\

# >>> SCRIPT_DIR.parents[2]
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web')
