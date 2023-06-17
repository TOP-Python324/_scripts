def test_func(pos_key1, pos_key2, *, key1, key2):
    print(pos_key1, pos_key2, key1, key2, sep='\n', end='\n\n')



test_func(10, 20, key1=30, key2=40)
# 10
# 20
# 30
# 40

test_func(10, key1=20, key2=30, pos_key2=40)
# 10
# 40
# 20
# 30

test_func(key1=10, key2=20, pos_key2=30, pos_key1=40)
# 40
# 30
# 10
# 20

# test_func(10, 20, 30, 40)
# ... TypeError: test_func() takes 2 positional arguments but 4 were given


def write_musicfile_in_db(
        musicfile: bytes,
        audio_format: str,
        *,
        sample_rate: int,
        bit_depth: int,
        channels: int,
        year: int,
        track_name: str,
        artist: str,
        album: str = None,
):
    """Записывает в БД музыкальный файл и его метаинформацию."""


# неудобно
write_musicfile_in_db(
    b'FFFFFFFF',
    'WAV',
    44100,
    8,
    6,
    2010,
    'Bom-Bom',
    'Boomer',
    'BOOM',
)
# удобно
write_musicfile_in_db(
    b'FFFFFFFF',
    'WAV',
    sample_rate=44100,
    bit_depth=8,
    channels=6,
    year=2010,
    track_name='Bom-Bom',
    artist='Boomer',
    album='BOOM',
)
