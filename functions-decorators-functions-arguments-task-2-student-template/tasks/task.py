def union(*args) -> set:
    result_set = set()

    for collection in args:
        result_set = result_set | set(collection)

    return result_set


def intersect(*args) -> set:
    result_set = set(args[0]) if args else set()

    for collection in args:
        result_set = result_set & set(collection)

    return result_set


if __name__ == '__main__':
    res_union = union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
    print(res_union)
    assert res_union == {'S', 'P', 'A', 'M', 'C'}

    res_intersect = intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
    print(res_intersect)
    assert res_intersect == {'S', 'C'}
