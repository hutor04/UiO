import random


def my_sampler(data, slices_size, fixed_seed=True):
    if fixed_seed:
        random.seed(42)
    data_length = len(data)
    indexes = list(range(data_length))
    random.shuffle(indexes)
    items_per_slice = [int(data_length * slice) for slice in slices_size]
    result = []
    start = 0

    for i in items_per_slice:
        slice_items = []
        stop = start + i
        for el in indexes[start:stop]:
            slice_items.append(data[el])
        result.append(slice_items)
        start = stop
    return result
