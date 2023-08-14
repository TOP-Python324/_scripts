from sys import path


print(*path, sep='\n')
# каталоги, в которых осуществляется поиск модулей во время импорта
# D:\G-Doc\TOP Academy\Python web\324\scripts\base
# G:\Python311\python311.zip
# G:\Python311\DLLs
# G:\Python311\Lib
# G:\Python311
# G:\Python311\Lib\site-packages
# G:\Python311\Lib\site-packages\win32
# G:\Python311\Lib\site-packages\win32\lib
# G:\Python311\Lib\site-packages\Pythonwin

try:
    import conf
except ModuleNotFoundError:
    print('файл conf.py отсутствует в каталогах sys.path')
