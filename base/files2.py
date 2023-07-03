from pathlib import Path
from sys import path


SCRIPT_DIR = Path(path[0])
filein_path = SCRIPT_DIR / '_direct_import.py'

filein = open(filein_path, encoding='utf-8')

for line in filein:
    print(repr(line))

filein.close()


with open(filein_path, encoding='utf-8') as filein:
    text = filein.read()

with open(filein_path, encoding='utf-8') as filein:
    lines = filein.readlines()

comments = [line.strip() for line in lines if line.startswith('#')]
comments = '\n\n'.join(comments)

with open(SCRIPT_DIR / '_direct_import.comments', 'w', encoding='utf-8') as fileout:
    # fileout.writelines(comments)
    fileout.write(comments)

