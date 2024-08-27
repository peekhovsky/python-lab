class PriceControl:
    def __init__(self):
        self.price = 0

    def __get__(self, instance, owner):
        return self.price

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.price = value

    def __delete__(self, instance):
        del self.price


class NameControl:
    def __init__(self, name):
        self.name = name
        self.is_set = False

    def __get__(self, instance, owner):
        if not self.is_set:
            raise ValueError("Not initialized")
        return self.name

    def __set__(self, instance, value):
        if self.is_set:
            raise ValueError(F'{self.name} can not be changed.')
        self.name = value
        self.is_set = True

    def __delete__(self, instance):
        del self.name


class Book:
    author = NameControl('Author')
    name = NameControl('Name')
    price = PriceControl()

    def __init__(self, author, name, price):
        self.name = name
        self.author = author
        self.price = price


if __name__ == '__main__':
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
    assert (f"Author='{b.author}', Name='{b.name}', Price='{b.price}'"
            == "Author='William Faulkner', Name='The Sound and the Fury', Price='12'")

    b.price = 55
    assert b.price == 55
