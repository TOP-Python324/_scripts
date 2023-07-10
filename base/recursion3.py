data1 = [
    1,
    2,
    'abc',
    ('x', 'y', 'z'),
    5,
    [(0.1, 0.2), (0.1, 0.3), (-0.2, 0.1)],
    7
]
data2 = [
    0.1,
    0.2,
    {
        'i': 15,
        'j': 20,
        'k': -4
    },
    (
        {'z', 'o', 'v'},
        {'a', 'b'},
    ),
    0.3,
    [
        {
            2000: ('event1', 'event2'),
            2010: ('event1', 'event2', 'event3'),
        },
        {
            'city1': 1.21*10**6,
            'city2': 2.9*10**6,
        }
    ]
]


from collections.abc import Iterable


def flatten(data: Iterable) -> list:
    result = []
    
    if isinstance(data, dict):
        data = data.values()
    
    for elem in data:
        if isinstance(elem, Iterable) and not isinstance(elem, str):
            result += flatten(elem)
        else:
            result += [elem]
    
    return result


# >>> flatten(data1)
# [1, 2, 'abc', 'x', 'y', 'z', 5, 0.1, 0.2, 0.1, 0.3, -0.2, 0.1, 7]
# >>>
# >>> flatten(data2)
# [0.1, 0.2, 15, 20, -4, 'z', 'o', 'v', 'b', 'a', 0.3, 'event1', 'event2', 'event1', 'event2', 'event3', 1210000.0, 2900000.0]
