# абсолютные пути
# d:\scripts\python\test.py
# /home/user/scripts/python/test.py

# относительные пути

# cwd (текущий рабочий каталог) d:\G-Doc\YandexDisk\Job\TOP Academy\Python web
# 324\scipts\path1.py

# cwd (текущий рабочий каталог) /home/user
# documents/project1/architecture.txt


# никаких проблем
'/home/user/scripts/python/test.py'

# экранированные последовательности
bad_path1 = 'd:\scripts\python\test.py'

good_path1 = 'd:\\scripts\\python\\test.py'
good_path2 = r'd:\scripts\python\test.py'

# bad_path2 = r'd:\scripts\python\'

good_path3 = r'd:\programs\python2.7.tar.gz'
