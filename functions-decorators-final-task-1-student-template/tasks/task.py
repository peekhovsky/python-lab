def split(data: str, sep=None, maxsplit=-1):
    left_data = trim_data(data, sep or ' ')
    return do_split(left_data, sep or ' ', len(left_data) - 1 if maxsplit == -1 else maxsplit)


def get_slice_end(data: str, separator):
    slice_end = data.find(separator)
    if slice_end >= 0:
        return slice_end, False
    else:
        return len(data), True


def do_split(data: str, separator, maxsplit):
    result = []

    slice_num = 0

    left_data = trim_data(data, separator)

    while slice_num <= maxsplit:
        if slice_num == maxsplit:
            result.append(left_data)
            break

        slice_end, is_last = get_slice_end(left_data, separator)
        slice_data = left_data[:slice_end]
        result.append(slice_data)

        if is_last:
            break

        left_data = trim_data(left_data[(len(slice_data) + len(separator)):], separator)
        slice_num += 1

    print(f'result: {result}')
    return result


def trim_data(data: str, separator: str):
    if separator.isspace():
        return data.lstrip()
    return str(data)


if __name__ == '__main__':
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']
    assert split('') == []
    assert split(' ', sep=',') == [' ']
    assert split(' ') == []
