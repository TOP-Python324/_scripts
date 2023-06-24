def range_pairs(start, stop, step=1):
    for n in range(start, stop, step):
        yield n
        yield n


def infinite_counter(start, step=1):
    while True:
        yield start
        start += step

