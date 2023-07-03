from pathlib import Path
from re import compile
from sys import path


filename_pattern = compile(r'_\w+\.py')

SCRIPT_DIR = Path(path[0])
fileout_path = SCRIPT_DIR / 'files3.log'

for file in SCRIPT_DIR.iterdir():
    if filename_pattern.fullmatch(file.name):
        with open(fileout_path, 'a') as fileout:
            fileout.write(f'{file.name}\n')

