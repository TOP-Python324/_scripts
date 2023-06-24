def test_func(pos1, pos2, /, pos_key1, pos_key2):
    print(pos1, pos2, pos_key1, pos_key2, sep='\n', end='\n\n')


test_func(10, 20, 30, 40)
# 10
# 20
# 30
# 40

test_func(10, 20, pos_key2=30, pos_key1=40)
# 10
# 20
# 40
# 30

# test_func(10, pos2=20, pos_key2=30, pos_key1=40)
# ... TypeError: test_func() got some positional-only arguments passed as keyword arguments: 'pos2'


def point_checker(x, y, /, algorithm='h', switch=True):
    pass


# point_checker(algorithm='z', x=5, y=1)
# point_checker(y=2, x=6, algorithm='z')

point_checker(5, 1)
point_checker(5, 2, algorithm='z')
point_checker(3, 6, switch=False)
