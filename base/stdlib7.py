from csv import reader, writer
from pathlib import Path
from pprint import pprint
from random import randrange as rr
from sys import path


SCRIPT_DIR = Path(path[0])


matrix = [
    [rr(10) for _ in range(6)]
    for _ in range(5)
]
pprint(matrix)
print()

data_path = SCRIPT_DIR / 'stdlib7.csv'
with open(data_path, 'w', encoding='utf-8') as data_file:
    csv_file = writer(data_file, lineterminator='\n')
    for row in matrix:
        csv_file.writerow(row)

with open(data_path, encoding='utf-8') as data_file:
    data = reader(data_file)
    data = [
        [int(n) for n in row]
        for row in data
    ]
pprint(matrix)
print()
