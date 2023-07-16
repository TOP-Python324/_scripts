from json import load, loads, dump, dumps
from pathlib import Path
from pprint import pprint
from sys import path


script_dir = Path(path[0])
data_path1 = script_dir / 'stdlib8_1.json'
data_path2 = script_dir / 'stdlib8_2.json'


json_text = data_path1.read_text(encoding='utf-8')
data = loads(json_text)

pprint(data)
print()

data[2]['points'] += [
    '_p_rocks',
    '_p_rocks_predator_attack',
    '_p_fall',
]

json_text = dumps(data, ensure_ascii=False)
print(f'{json_text = }\n')

with open(data_path2, 'w', encoding='utf-8') as data_file2:
    dump(data, data_file2, ensure_ascii=False, indent=2)

with open(data_path2, encoding='utf-8') as data_file2:
    data = load(data_file2)

pprint(data)
