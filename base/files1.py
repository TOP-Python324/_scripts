from pathlib import Path
from sys import path


SCRIPT_DIR = Path(path[0])
filein_path = SCRIPT_DIR / 'walrus1.py'

text = filein_path.read_text(encoding='utf-8')

comments = text.split('\n')
comments = filter(lambda line: line.startswith('#'), comments)
comments = '\n\n'.join(comments)

fileout_path = SCRIPT_DIR / 'walrus1_comments'

fileout_path.write_text(comments, encoding='utf-8')
