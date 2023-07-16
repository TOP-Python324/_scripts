from pathlib import Path
from pprint import pprint
from sys import path
from tomllib import load, loads


config_path = Path(path[0]) / 'stdlib9.toml'


data = loads(config_path.read_text(encoding='utf-8'))

pprint(data)
