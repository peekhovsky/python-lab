from __future__ import annotations
from typing import Type


class Currency:
    course_value = None
    abbr = None

    def __init__(self, value: float):
        self.value = value

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        value = other_cls.get_value(self)
        return other_cls.new_object(value)

    @classmethod
    def new_object(cls, value: float) -> Currency:
        raise Exception("not implemented")

    @classmethod
    def get_value(cls, other: Currency) -> float:
        return other.value * (other.course_value / cls.course_value)

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return f"{cls.course_value / other_cls.course_value} {other_cls.abbr} for 1 {cls.abbr}"

    def __str__(self):
        return f"{self.value} {self.abbr}"

    def __add__(self, other: Currency) -> Currency:
        other_value = self.get_value(other)
        return self.new_object(self.value + other_value)

    def __eq__(self, other):
        other_value = self.get_value(other)
        return self.value == other_value

    def __ne__(self, other):
        other_value = self.get_value(other)
        return self.value != other_value

    def __lt__(self, other):
        other_value = self.get_value(other)
        return self.value < other_value

    def __gt__(self, other):
        other_value = self.get_value(other)
        return self.value > other_value

    def __le__(self, other):
        other_value = self.get_value(other)
        return self.value <= other_value

    def __ge__(self, other):
        other_value = self.get_value(other)
        return self.value >= other_value


# 1 EUR = 2 USD = 100 GBP
class Euro(Currency):
    course_value = 100.0
    abbr = 'EUR'

    @classmethod
    def new_object(cls, value: float):
        return Euro(value)


class Dollar(Currency):
    course_value = 50.0
    abbr = 'USD'

    @classmethod
    def new_object(cls, value: float):
        return Dollar(value)


class Pound(Currency):
    course_value = 1.0
    abbr = 'GBP'

    @classmethod
    def new_object(cls, value: float):
        return Pound(value)


if __name__ == '__main__':
    res = Euro.course(Pound)
    print(f'res={res}')
    assert res == "100.0 GBP for 1 EUR"

    res = Dollar.course(Pound)
    print(f'res={res}')
    assert res == "50.0 GBP for 1 USD"

    res = Pound.course(Euro)
    print(f'res={res}')
    assert res == "0.01 EUR for 1 GBP"

    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    res = e.to_currency(Dollar)
    print(f'res={res}')
    assert str(res) == "200.0 USD"

    res = e.to_currency(Pound)
    print(f'res={res}')
    assert str(res) == "10000.0 GBP"

    res = e.to_currency(Euro)
    print(f'res={res}')
    assert str(res) == "100.0 EUR"

    res = r.to_currency(Dollar)
    print(f'res={res}')
    assert str(res) == "2.0 USD"

    res = r.to_currency(Euro)
    print(f'res={res}')
    assert str(res) == "1.0 EUR"

    res = r.to_currency(Pound)
    print(f'res={res}')
    assert str(res) == "100.0 GBP"

    res = e + r
    print(f'res={res}')
    assert str(res) == "101.0 EUR"

    res = r + d
    print(f'res={res}')
    assert str(res) == "10100.0 GBP"

    res = d + e
    print(f'res={res}')
    assert str(res) == "400.0 USD"
