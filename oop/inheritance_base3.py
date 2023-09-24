from numbers import Number

# storage = DictOfRanges({
#     (1, 10): 'мало',
#     (11, 70): 'нормально',
#     (71, 100): 'много'
# })
# storage[5] --> 'мало'
# storage[(1, 10)] --> 'мало'


class DictOfRanges(dict):
    def __getitem__(self, key):
        if isinstance(key, Number):
            for key_range, value in self.items():
                left, right = key_range
                if left <= key <= right:
                    return value
            else:
                raise KeyError
        else:
            return super().__getitem__(key)

