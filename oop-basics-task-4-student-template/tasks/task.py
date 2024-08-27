from typing import Dict


class HistoryDict:
    def __init__(self, dictionary: Dict[str, int]):
        self.dictionary = dictionary
        self.last_changed_keys = []

    def get_history(self):
        return self.last_changed_keys

    def set_value(self, key, value):
        self.dictionary.update({key: value})
        self.last_changed_keys.append(key)
        self.last_changed_keys = self.last_changed_keys[-5:]


if __name__ == '__main__':
    d = HistoryDict({"foo": 42})
    d.set_value("bar1", 43)
    res = d.get_history()

    print(f'res: {res}')
    assert res == ['bar1']

    d.set_value("bar2", 43)
    d.set_value("bar3", 43)
    d.set_value("bar4", 43)
    d.set_value("bar5", 43)
    d.set_value("bar6", 43)

    res = d.get_history()
    print(f'res: {res}')
    assert res == ['bar2', 'bar3', 'bar4', 'bar5', 'bar6']

    d = HistoryDict({})
    d.set_value("b", 41)
    d.set_value("c", 42)
    d.set_value("b", 43)
    d.set_value("c", 44)
    d.set_value("d", 45)

    res = d.get_history()
    print(f'res: {res}')
