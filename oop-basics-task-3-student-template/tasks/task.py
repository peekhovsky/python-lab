class Counter:

    def __init__(self, start=0, stop=None):
        self.counter = start
        self.stop = stop

    def increment(self):
        if self.stop is not None and self.counter >= self.stop:
            print('Maximal value is reached.')
        else:
            self.counter += 1

    def get(self):
        return self.counter


if __name__ == '__main__':
    c = Counter(start=42)
    c.increment()
    res = c.get()
    print(f'res: {res}')
    assert res == 43

    c = Counter()
    c.increment()
    res = c.get()
    print(f'res: {res}')
    assert res == 1

    c.increment()
    res = c.get()
    print(f'res: {res}')
    assert res == 2

    c = Counter(start=42, stop=43)
    c.increment()
    res = c.get()
    print(f'res: {res}')
    assert res == 43

    c.increment()
    res = c.get()
    print(f'res: {res}')
    assert res == 43
